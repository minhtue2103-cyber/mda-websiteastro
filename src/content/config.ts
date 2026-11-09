import { defineCollection, z } from 'astro:content';

// 1. Collection Tin Tức (/tin-tuc/[slug]) -> Headline Photo + Content (Không yêu cầu Category)
const newsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishDate: z.string(),
    updatedDate: z.string().optional(),
    headlinePhoto: z.string(),
    headlinePhotoAlt: z.string(),
    headlinePhotoCaption: z.string().optional(),
    author: z.string().default('Ban Biên Tập Pháp Lý & XNK MDA'),
    featured: z.boolean().default(false),
  }),
});

// 2. Collection Blog (/blog/[slug]) -> Headline Photo + Category + Content + GEO Schema
const blogCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishDate: z.string(),
    updatedDate: z.string().optional(),
    category: z.enum([
      'Chứng Từ & Pháp Lý XNK',
      'Đào Tạo XNK Thực Chiến',
      'Ứng Dụng AI Trong XNK',
      'AI Marketing Quốc Tế',
    ]),
    headlinePhoto: z.string(),
    headlinePhotoAlt: z.string(),
    headlinePhotoCaption: z.string().optional(),
    author: z.string().default('Tuệ Phạm (Mr. Tuệ)'),
    readingTime: z.string().default('6 phút đọc'),
    tags: z.array(z.string()).default([]),
    faqSchema: z
      .array(
        z.object({
          question: z.string(),
          answer: z.string(),
        })
      )
      .optional(),
    sources: z
      .array(
        z.object({
          title: z.string(),
          url: z.string().url(),
        })
      )
      .optional(),
  }),
});

export const collections = {
  news: newsCollection,
  blog: blogCollection,
};

