'use strict';

hexo.extend.helper.register('generatePageTitle', function(page) {
  const config = this.config;
  const siteTitle = config.title || '';
  const subtitle = config.subtitle || '';
  let pageTitle = '';

  if (this.is_archive()) {
    pageTitle = this.__('page.archive');
  } else if (this.is_tag()) {
    pageTitle = page.tag;
  } else if (this.is_category()) {
    pageTitle = page.category;
  } else if (this.is_post() || this.is_page()) {
    pageTitle = page.title;
  }

  if (this.is_home()) {
    if (siteTitle && subtitle) {
      return `${siteTitle} | ${subtitle}`;
    } else if (siteTitle) {
      return siteTitle;
    } else if (subtitle) {
      return subtitle;
    }
  } else {
    if (pageTitle) {
      return `${pageTitle} | ${siteTitle}`;
    } else {
      return siteTitle;
    }
  }
});

hexo.extend.helper.register('generateJSONLD', function (page) {
  const config = this.config;
  const theme = this.theme;

  let jsonld = {};
  if (this.is_post()) {
    jsonld = {
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": this.full_url_for(page.path)
      },
      "headline": page.title,
      "description": (page.description || page.excerpt || page.content || '')
        .replace(/<[^>]*>/g, '') // striptags
        .replace(/\n+/g, ' ')
        .trim()
        .substring(0, 160),
      "datePublished": page.date.toISOString(),
      "dateModified": page.updated.toISOString(),
      "author": {
        "@type": "Person",
        "name": config.author || theme.author || 'Unknown Author',
        "url": this.full_url_for('about/'),
        "sameAs": ["https://github.com/Th1s1sYukia"]
      },
      "publisher": {
        "@type": "Person",
        "name": config.author || theme.author || 'Unknown Author',
        "url": this.full_url_for('about/')
      }
    };
    if (page.cover || page.thumbnail) {
      jsonld.image = page.cover || page.thumbnail;
    }
  } else if (this.is_home()) {
    jsonld = {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "WebSite",
          "@id": `${config.url}/#website`,
          "name": config.title,
          "description": config.description,
          "url": config.url,
          "inLanguage": config.language
        },
        {
          "@type": "Person",
          "@id": `${config.url}/about/#person`,
          "name": config.author || '朱宇锴（Yukia）',
          "url": this.full_url_for('about/'),
          "sameAs": ["https://github.com/Th1s1sYukia"],
          "knowsAbout": ["独立站 SEO", "海外内容运营", "Digital Growth"]
        }
      ]
    };
  } else if (this.is_category() || this.is_tag() || this.is_archive()) {
    jsonld = {
      "@context": "https://schema.org",
      "@type": "CollectionPage",
      "name": page.title || 'set of articles',
      "url": this.full_url_for(page.path)
    };
  } else {
    jsonld = {
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": page.title,
      "url": this.full_url_for(page.path)
    };
  }

  return `<script type="application/ld+json">\n${JSON.stringify(jsonld)}\n</script>`;
});
