#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
MEKONG DELTA AGRI (MDA HUB) — MEDIA WEBP CONVERTER & GIT SYNC
=============================================================================
Mục đích:
1. Quét toàn bộ file ảnh (.jpg, .jpeg, .png) trong folder media (mặc định: public/media).
2. Chuyển đổi sang định dạng .webp chuẩn (giữ kênh alpha RGBA, nén chất lượng cao).
3. Tìm và thay thế đường dẫn ảnh nội bộ trong toàn bộ mã nguồn (src/**/*.astro, ts, js, md, v.v.),
   tuyệt đối KHÔNG thay thế các URL bên ngoài (http://, https://, //).
4. Cập nhật .gitignore để loại trừ các file .jpg, .jpeg, .png trong thư mục media.
5. Kiểm tra danh sách file thay đổi, bảo đảm KHÔNG stage file .jpg/.png, và commit lên git.
6. Tự động push commit lên git remote (mặc định: origin / nhánh hiện tại).
=============================================================================
"""

import os
import sys
import re
import argparse
import subprocess
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("[ERROR] Thư viện Pillow chưa được cài đặt. Vui lòng chạy: pip install Pillow")
    sys.exit(1)


# Các định dạng ảnh cần convert
SOURCE_EXTENSIONS = {'.jpg', '.jpeg', '.png'}

# Thư mục mã nguồn cần quét & thay thế đường dẫn
SOURCE_DIRS = ['src', 'public']

# Các phần mở rộng file mã nguồn cần quét
CODE_EXTENSIONS = {'.astro', '.ts', '.js', '.jsx', '.tsx', '.json', '.md', '.mdx', '.html', '.css', '.txt'}


def convert_image_to_webp(input_path: Path, output_path: Path, quality: int = 85) -> dict:
    """
    Chuyển đổi 1 file ảnh sang định dạng WebP với xử lý màu sắc và kênh alpha an toàn.
    """
    orig_size = input_path.stat().st_size
    with Image.open(input_path) as img:
        # Xử lý kênh màu: nếu ảnh có transparency (P hoặc RGBA) thì giữ RGBA, nếu không thì RGB
        if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
            img = img.convert("RGBA")
        elif img.mode != "RGB":
            img = img.convert("RGB")

        # Lưu ảnh dưới định dạng WEBP
        output_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(output_path, "WEBP", quality=quality, method=6)

    new_size = output_path.stat().st_size
    savings = (1 - (new_size / orig_size)) * 100 if orig_size > 0 else 0

    return {
        "input": input_path,
        "output": output_path,
        "orig_size": orig_size,
        "new_size": new_size,
        "savings": savings,
    }


def find_and_convert_media(media_dir: Path, quality: int = 85, dry_run: bool = False) -> dict:
    """
    Quét folder media và convert tất cả ảnh .jpg/.png sang .webp.
    Trả về mapping từ tên file cũ sang tên file mới.
    """
    conversions = []
    replacement_map = {}  # { 'profile-jen-pham.jpg': 'profile-jen-pham.webp', ... }

    print(f"\n[1/6] Quét thư mục media: {media_dir}")
    if not media_dir.exists():
        print(f"[WARN] Thư mục media '{media_dir}' không tồn tại!")
        return replacement_map

    for root, _, files in os.walk(media_dir):
        for file in files:
            file_path = Path(root) / file
            ext = file_path.suffix.lower()

            if ext in SOURCE_EXTENSIONS:
                webp_path = file_path.with_suffix('.webp')
                rel_old = file_path.relative_to(media_dir.parent).as_posix()
                rel_new = webp_path.relative_to(media_dir.parent).as_posix()

                # Lưu mapping cả tên file đơn lẻ và đường dẫn relative (/media/...)
                replacement_map[file] = webp_path.name
                replacement_map[f"/{rel_old}"] = f"/{rel_new}"
                replacement_map[rel_old] = rel_new

                if not dry_run:
                    result = convert_image_to_webp(file_path, webp_path, quality=quality)
                    conversions.append(result)
                    print(f"  -> Converted: {file} ({result['orig_size'] // 1024}KB) -> {webp_path.name} ({result['new_size'] // 1024}KB, -{result['savings']:.1f}%)")
                else:
                    print(f"  [DRY RUN] Will convert: {file} -> {webp_path.name}")

    print(f"[OK] Đã hoàn tất convert {len(replacement_map) // 3} ảnh sang .webp.")
    return replacement_map


def is_part_of_external_url(content: str, start_pos: int) -> bool:
    """
    Kiểm tra xem vị trí start_pos có nằm trong một URL ngoại bộ (bắt đầu bằng http://, https://, hoặc //) hay không.
    """
    delims = set("\"'`()<>{} \t\r\n")
    idx = start_pos - 1
    while idx >= 0 and (start_pos - idx) < 500:
        if content[idx] in delims:
            break
        idx -= 1
    token_start = idx + 1
    prefix = content[token_start:start_pos].lstrip()
    return prefix.startswith(('http://', 'https://', '//'))


def safe_replace_image_link(content: str, old_ref: str, new_ref: str) -> tuple[str, int]:
    """
    Thay thế chuỗi old_ref thành new_ref trong content, chỉ áp dụng cho link nội bộ,
    bỏ qua các vị trí nằm trong URL ngoại bộ (http://, https://, //).
    Không dùng lookbehind regex phức tạp để tương thích 100% với Python 3.11 và mọi phiên bản.
    """
    if old_ref not in content:
        return content, 0

    result = []
    last_idx = 0
    count = 0
    len_old = len(old_ref)

    while True:
        idx = content.find(old_ref, last_idx)
        if idx == -1:
            result.append(content[last_idx:])
            break

        # Kiểm tra xem vị trí xuất hiện có nằm trong URL ngoại bộ không
        if is_part_of_external_url(content, idx):
            result.append(content[last_idx:idx + len_old])
        else:
            result.append(content[last_idx:idx])
            result.append(new_ref)
            count += 1

        last_idx = idx + len_old

    return "".join(result), count


def replace_image_links_in_source(workspace_root: Path, replacement_map: dict, dry_run: bool = False) -> list:
    """
    Quét mã nguồn và thay thế các link ảnh nội bộ sang .webp.
    Bỏ qua các link ảnh ngoại tuyến (bắt đầu bằng http://, https://, //).
    """
    print("\n[2/6] Quét và thay thế link ảnh nội bộ trong mã nguồn...")
    if not replacement_map:
        print("  Không có ảnh nào cần thay thế link.")
        return []

    modified_files = []

    # Thu thập tất cả các file mã nguồn cần quét
    files_to_scan = []
    for sdir in SOURCE_DIRS:
        scan_path = workspace_root / sdir
        if not scan_path.exists():
            continue
        for root, _, files in os.walk(scan_path):
            for file in files:
                p = Path(root) / file
                if p.suffix.lower() in CODE_EXTENSIONS:
                    files_to_scan.append(p)

    # Sắp xếp các chuỗi thay thế theo độ dài giảm dần để ưu tiên match đường dẫn dài trước
    sorted_replacements = sorted(replacement_map.keys(), key=len, reverse=True)

    for file_path in files_to_scan:
        try:
            content = file_path.read_text(encoding="utf-8")
        except Exception:
            continue

        original_content = content
        replacements_in_file = 0

        for old_ref in sorted_replacements:
            if old_ref not in content:
                continue

            new_ref = replacement_map[old_ref]
            content, count = safe_replace_image_link(content, old_ref, new_ref)
            replacements_in_file += count

        if content != original_content:
            rel_file = file_path.relative_to(workspace_root).as_posix()
            modified_files.append((rel_file, replacements_in_file))
            print(f"  -> Cập nhật link ({replacements_in_file} vị trí) trong: {rel_file}")
            if not dry_run:
                file_path.write_text(content, encoding="utf-8")

    print(f"[OK] Đã cập nhật link ảnh trong {len(modified_files)} file mã nguồn.")
    return modified_files


def ensure_gitignore_rules(workspace_root: Path, dry_run: bool = False) -> bool:
    """
    Cập nhật .gitignore để loại trừ các file ảnh .jpg/.png trong folder public/media.
    """
    print("\n[3/6] Kiểm tra và cập nhật quy tắc trong .gitignore...")
    gitignore_path = workspace_root / ".gitignore"

    rules = [
        "# Ignore raw raster images in media folder (only track .webp and .svg)",
        "public/media/*.jpg",
        "public/media/*.jpeg",
        "public/media/*.png",
        "public/media/**/*.jpg",
        "public/media/**/*.jpeg",
        "public/media/**/*.png",
    ]

    existing_content = ""
    if gitignore_path.exists():
        existing_content = gitignore_path.read_text(encoding="utf-8")

    needs_update = False
    for rule in rules[1:]:
        if rule not in existing_content:
            needs_update = True
            break

    if needs_update:
        new_content = existing_content.rstrip() + "\n\n" + "\n".join(rules) + "\n"
        print("  -> Thêm quy tắc loại trừ .jpg, .png trong public/media vào .gitignore.")
        if not dry_run:
            gitignore_path.write_text(new_content, encoding="utf-8")
        return True
    else:
        print("  -> .gitignore đã có sẵn các quy tắc loại trừ.")
        return False


def run_git_command(args: list, cwd: Path) -> str:
    """Thực thi lệnh git an toàn và trả về output chuỗi."""
    res = subprocess.run(args, cwd=str(cwd), capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Lệnh git thất bại: {' '.join(args)}\nError: {res.stderr}")
    return res.stdout.strip()


def get_current_git_branch(workspace_root: Path) -> str:
    """Lấy tên nhánh git hiện tại."""
    try:
        branch = run_git_command(["git", "branch", "--show-current"], cwd=workspace_root)
        if branch:
            return branch
    except Exception:
        pass
    try:
        branch = run_git_command(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=workspace_root)
        if branch and branch != "HEAD":
            return branch
    except Exception:
        pass
    return "main"


def push_to_git(workspace_root: Path, remote: str = "origin", branch: str = None, dry_run: bool = False) -> bool:
    """
    Tự động push commit lên git remote (mặc định: origin / nhánh hiện tại).
    """
    target_branch = branch or get_current_git_branch(workspace_root)
    print(f"\n[6/6] Tự động push lên remote git ({remote}/{target_branch})...")

    if dry_run:
        print(f"  [DRY RUN] Bỏ qua thực thi: git push {remote} {target_branch}")
        return True

    try:
        print(f"  -> Đang thực hiện: git push {remote} {target_branch}...")
        res = subprocess.run(
            ["git", "push", remote, target_branch],
            cwd=str(workspace_root),
            capture_output=True,
            text=True
        )
        if res.returncode == 0:
            output = (res.stdout + "\n" + res.stderr).strip()
            print(f"[THÀNH CÔNG] Đã push thành công lên {remote}/{target_branch}!")
            if output:
                for line in output.splitlines():
                    if line.strip():
                        print(f"  {line}")
            return True
        else:
            err_msg = res.stderr.strip() or res.stdout.strip()
            print(f"[LỖI PUSH] Không thể push lên {remote}/{target_branch}:")
            print(f"  {err_msg}")
            print(f"  -> Gợi ý: Hãy kiểm tra kết nối mạng hoặc thử chạy thủ công: git push {remote} {target_branch}")
            return False
    except Exception as ex:
        print(f"[LỖI PUSH] Lỗi ngoại lệ khi thực hiện git push: {ex}")
        return False


def check_and_commit_git(
    workspace_root: Path,
    auto_push: bool = True,
    remote: str = "origin",
    branch: str = None,
    dry_run: bool = False
) -> bool:
    """
    Kiểm tra trạng thái git, stage các file hợp lệ (.webp, code, .gitignore),
    bảo đảm không stage file .jpg/.png, sau đó commit và tự động push lên git.
    """
    print("\n[4/6] Kiểm tra danh sách file thay đổi (Git Status)...")
    status_output = run_git_command(["git", "status", "--porcelain"], cwd=workspace_root)

    committed = False
    if not status_output:
        print("  Không có file nào thay đổi cần commit.")
    else:
        print("--- Trạng thái thay đổi hiện tại ---")
        for line in status_output.splitlines():
            print(f"  {line}")

        if dry_run:
            print("\n[DRY RUN] Bỏ qua bước stage & commit git.")
        else:
            print("\n[5/6] Tiến hành stage & commit các file hợp lệ...")

            # Stage file .gitignore nếu có thay đổi
            if (workspace_root / ".gitignore").exists():
                run_git_command(["git", "add", ".gitignore"], cwd=workspace_root)

            # Stage các file .webp (dùng Python rglob để lấy danh sách file thực tế, tránh lỗi pathspec wildcard trên Windows)
            media_path = workspace_root / "public" / "media"
            if media_path.exists():
                webp_files = [p.relative_to(workspace_root).as_posix() for p in media_path.rglob("*.webp")]
                if webp_files:
                    run_git_command(["git", "add"] + webp_files, cwd=workspace_root)

            # Stage các file mã nguồn đã sửa link
            if (workspace_root / "src").exists():
                run_git_command(["git", "add", "src/"], cwd=workspace_root)

            # Stage thư mục scripts
            if (workspace_root / "scripts").exists():
                run_git_command(["git", "add", "scripts/"], cwd=workspace_root)

            # Stage thư mục tài liệu document nếu có
            doc_path = workspace_root / "public" / "media" / "document"
            if doc_path.exists():
                run_git_command(["git", "add", "public/media/document/"], cwd=workspace_root)

            # Kiểm tra các file đã staged
            staged_output = run_git_command(["git", "diff", "--name-only", "--cached"], cwd=workspace_root)
            staged_files = [f for f in staged_output.splitlines() if f.strip()]

            # Kiểm tra an toàn: Tuyệt đối không stage file .jpg hay .png
            forbidden_staged = [f for f in staged_files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
            if forbidden_staged:
                print(f"[CẢNH BÁO] Phát hiện {len(forbidden_staged)} file .jpg/.png bị stage nhầm. Đang tự động unstage:")
                for f in forbidden_staged:
                    print(f"  -> Unstage: {f}")
                    run_git_command(["git", "reset", "HEAD", "--", f], cwd=workspace_root)

                # Lấy lại danh sách sau khi unstage
                staged_output = run_git_command(["git", "diff", "--name-only", "--cached"], cwd=workspace_root)
                staged_files = [f for f in staged_output.splitlines() if f.strip()]

            if not staged_files:
                print("  Không có file hợp lệ nào để commit.")
            else:
                print(f"\n[OK] Danh sách {len(staged_files)} file sẵn sàng commit:")
                for f in staged_files:
                    print(f"  + {f}")

                commit_msg = "perf: optimize media to webp, update internal image references and ignore raw jpg/png"
                commit_res = run_git_command(["git", "commit", "-m", commit_msg], cwd=workspace_root)
                print(f"\n[THÀNH CÔNG] Git commit hoàn tất:\n{commit_res}")
                committed = True

    # Tự động push nếu được bật (áp dụng khi vừa commit mới hoặc có thay đổi chưa push)
    if auto_push:
        push_to_git(workspace_root, remote=remote, branch=branch, dry_run=dry_run)
    else:
        print("\n[INFO] Đã bỏ qua bước push git theo cờ --no-push.")
        target_branch = branch or get_current_git_branch(workspace_root)
        print(f"[GỢI Ý] Để đẩy lên remote thủ công, bạn có thể chạy: git push {remote} {target_branch}")

    return committed


def main():
    parser = argparse.ArgumentParser(description="Chuyển đổi ảnh media sang .webp, cập nhật mã nguồn, commit và tự động push git an toàn.")
    parser.add_argument("--media-dir", default="public/media", help="Đường dẫn thư mục media (mặc định: public/media)")
    parser.add_argument("--quality", type=int, default=85, help="Chất lượng nén WebP từ 1 đến 100 (mặc định: 85)")
    parser.add_argument("--dry-run", action="store_true", help="Chạy thử nghiệm không ghi đè file và không commit/push git")
    parser.add_argument("--no-commit", action="store_true", help="Chỉ convert và sửa link, không commit hoặc push git")
    parser.add_argument("--no-push", action="store_true", help="Chỉ commit, không tự động push lên remote git")
    parser.add_argument("--remote", default="origin", help="Tên remote git (mặc định: origin)")
    parser.add_argument("--branch", default=None, help="Tên nhánh git cần push (mặc định: nhánh hiện tại)")

    args = parser.parse_args()

    workspace_root = Path(__file__).resolve().parent.parent
    media_dir = workspace_root / args.media_dir

    print("=" * 70)
    print(" MDA HUB — BỘ CÔNG CỤ TỐI ƯU HÓA MEDIA SANG WEBP & GIT SYNC")
    print("=" * 70)
    print(f"Workspace: {workspace_root}")
    print(f"Media dir: {media_dir}")
    print(f"Quality:   {args.quality}")
    print(f"Dry run:   {args.dry_run}")
    print(f"Auto push: {not (args.no_commit or args.no_push)}")

    # Bước 1: Convert ảnh
    replacement_map = find_and_convert_media(media_dir, quality=args.quality, dry_run=args.dry_run)

    # Bước 2: Thay thế link trong source
    replace_image_links_in_source(workspace_root, replacement_map, dry_run=args.dry_run)

    # Bước 3: Đảm bảo .gitignore loại trừ jpg/png
    ensure_gitignore_rules(workspace_root, dry_run=args.dry_run)

    # Bước 4 & 5 & 6: Kiểm tra git status, commit và push
    if not args.no_commit:
        check_and_commit_git(
            workspace_root,
            auto_push=not args.no_push,
            remote=args.remote,
            branch=args.branch,
            dry_run=args.dry_run
        )
    else:
        print("\n[INFO] Đã bỏ qua bước commit và push git theo cờ --no-commit.")

    print("\n" + "=" * 70)
    print(" HOÀN TẤT TOÀN BỘ QUY TRÌNH!")
    print("=" * 70)


if __name__ == "__main__":
    main()
