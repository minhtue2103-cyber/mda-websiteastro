import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export const GET: APIRoute = async ({ site }) => {
  const baseUrl = site ? site.toString().replace(/\/$/, '') : 'https://mekongdeltaagri.com';
  const currentDate = new Date().toISOString().split('T')[0];

  // 1. Static Pages
  const staticPages = [
    { url: `${baseUrl}/`, priority: '1.0', changefreq: 'daily' },
    { url: `${baseUrl}/gioi-thieu/`, priority: '0.8', changefreq: 'monthly' },
    { url: `${baseUrl}/dich-vu/`, priority: '0.9', changefreq: 'weekly' },
    { url: `${baseUrl}/dich-vu/dao-tao-xnk-1-1/`, priority: '0.9', changefreq: 'weekly' },
    { url: `${baseUrl}/dich-vu/dao-tao-chuyen-sau-doanh-nghiep/`, priority: '0.9', changefreq: 'weekly' },
    { url: `${baseUrl}/dich-vu/dao-tao-chuyen-sau-doanh-nghiep/ung-dung-ai-xnk/`, priority: '0.8', changefreq: 'monthly' },
    { url: `${baseUrl}/dich-vu/dao-tao-chuyen-sau-doanh-nghiep/ai-marketing/`, priority: '0.8', changefreq: 'monthly' },
    { url: `${baseUrl}/tin-tuc/`, priority: '0.8', changefreq: 'daily' },
    { url: `${baseUrl}/blog/`, priority: '0.8', changefreq: 'daily' },
    { url: `${baseUrl}/dang-ky-thu-khoa-hoc/`, priority: '0.9', changefreq: 'weekly' },
  ];

  // 2. Collection News
  const newsEntries = await getCollection('news');
  const newsPages = newsEntries.map((entry) => ({
    url: `${baseUrl}/tin-tuc/${entry.slug}/`,
    lastmod: entry.data.updatedDate || entry.data.publishDate || currentDate,
    priority: '0.7',
    changefreq: 'monthly',
  }));

  // 3. Collection Blog
  const blogEntries = await getCollection('blog');
  const blogPages = blogEntries.map((entry) => ({
    url: `${baseUrl}/blog/${entry.slug}/`,
    lastmod: entry.data.updatedDate || entry.data.publishDate || currentDate,
    priority: '0.8',
    changefreq: 'weekly',
  }));

  const allUrls = [
    ...staticPages.map((p) => ({ ...p, lastmod: currentDate })),
    ...newsPages,
    ...blogPages,
  ];

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.7">
${allUrls
  .map(
    (item) => `  <url>
    <loc>${item.url}</loc>
    <lastmod>${item.lastmod}</lastmod>
    <changefreq>${item.changefreq}</changefreq>
    <priority>${item.priority}</priority>
  </url>`
  )
  .join('\n')}
</urlset>`;

  return new Response(xml, {
    status: 200,
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
      'X-Robots-Tag': 'index, follow',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};

