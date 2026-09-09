<template>
  <div class="news">
    <div class="news__header">
      <h2 class="news__title">Останні новини коледжу</h2>
    </div>

    <!-- Стан завантаження -->
    <div v-if="loading && news.length === 0" class="news__state news__state--loading">
      <div class="news__spinner"></div>
      <p>Завантаження новин...</p>
    </div>

    <!-- Стан помилки -->
    <div v-else-if="error && news.length === 0" class="news__state news__state--error">
      <svg class="news__error-svg" viewBox="0 0 24 24" width="42" height="42" fill="none" stroke="#dc2626" stroke-width="2">
        <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z" />
        <line x1="12" y1="9" x2="12" y2="13" />
        <line x1="12" y1="17" x2="12.01" y2="17" />
      </svg>
      <p>{{ error }}</p>
      <button class="news__retry-btn" @click="fetchNews(true)">Спробувати знову</button>
    </div>

    <!-- Сітка новин -->
    <div v-else class="news__grid">
      <div
        v-for="post in news"
        :key="post.id"
        class="news-card"
        @click="openModal(post)"
      >
        <div class="news-card__media">
          <img
            :src="getFeaturedImage(post)"
            :alt="stripHtml(post.title?.rendered)"
            class="news-card__image"
            @error="handleImageError"
          />
          <div class="news-card__overlay"></div>
        </div>

        <div class="news-card__content">
          <div class="news-card__date">
            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="3" y="4" width="18" height="18" rx="2" ry="2" />
              <line x1="16" y1="2" x2="16" y2="6" />
              <line x1="8" y1="2" x2="8" y2="6" />
              <line x1="3" y1="10" x2="21" y2="10" />
            </svg>
            <span>{{ formatDate(post.date) }}</span>
          </div>
          <h3 class="news-card__title" v-html="post.title?.rendered"></h3>
          <span class="news-card__cta">Читати далі →</span>
        </div>
      </div>
    </div>

    <!-- Модальне вікно новини -->
    <Transition name="fade">
      <div
        v-if="isModalOpen && selectedPost"
        class="news-modal__overlay"
        @click.self="closeModal"
      >
        <div class="news-modal__content">
          <button class="news-modal__close-btn" @click="closeModal">&times;</button>

          <div class="news-modal__date">
            <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="3" y="4" width="18" height="18" rx="2" ry="2" />
              <line x1="16" y1="2" x2="16" y2="6" />
              <line x1="8" y1="2" x2="8" y2="6" />
              <line x1="3" y1="10" x2="21" y2="10" />
            </svg>
            <span>{{ formatDate(selectedPost.date) }}</span>
          </div>

          <div class="news-modal__header">
            <img
              v-if="getFeaturedImage(selectedPost)"
              :src="getFeaturedImage(selectedPost)"
              :alt="stripHtml(selectedPost.title?.rendered)"
              class="news-modal__image"
              @error="handleImageError"
            />
            <h3 class="news-modal__title" v-html="selectedPost.title?.rendered"></h3>
          </div>

          <div class="news-modal__body">
            <div
              class="news-modal__text"
              v-html="selectedPost.content?.rendered || selectedPost.excerpt?.rendered"
            ></div>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { fetchWithCache, getCachedData } from "../utils/cache";

const news = ref([]);
const loading = ref(true);
const error = ref(null);
const isModalOpen = ref(false);
const selectedPost = ref(null);

// Локальний вбудований SVG-плейсхолдер замість ненадійного via.placeholder.com
const defaultPlaceholder =
  'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="400" height="250" viewBox="0 0 400 250"><rect fill="%23e2e8f0" width="400" height="250"/><text fill="%2364748b" font-family="sans-serif" font-size="22" font-weight="bold" x="50%" y="50%" text-anchor="middle" dominant-baseline="middle">ОКСНАУ Новини</text></svg>';

const openModal = (post) => {
  selectedPost.value = post;
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
  setTimeout(() => {
    selectedPost.value = null;
  }, 250);
};

const fetchNews = async (forceRefresh = false) => {
  try {
    loading.value = true;
    error.value = null;

    // Швидке завантаження з кешу
    if (!forceRefresh) {
      const cached = getCachedData("https://ocsnau.net/wp-json/wp/v2/news?_embed=true&per_page=6&order=desc", true);
      if (cached && Array.isArray(cached) && cached.length > 0) {
        news.value = cached;
      }
    }

    // Запит з TTL 30 хвилин та автоматичним офлайн-кешем
    const endpoint = `https://ocsnau.net/wp-json/wp/v2/news?_embed=true&per_page=6&order=desc`;
    const data = await fetchWithCache(endpoint, {}, 1000 * 60 * 30);
    if (Array.isArray(data)) {
      news.value = data;
    }
  } catch (err) {
    if (news.value.length === 0) {
      error.value = "Не вдалося завантажити новини. Будь ласка, перевірте зв'язок з сервером.";
    }
    console.error("[News] Помилка завантаження:", err);
  } finally {
    loading.value = false;
  }
};

const getFeaturedImage = (post) => {
  if (
    post?._embedded &&
    post._embedded["wp:featuredmedia"] &&
    post._embedded["wp:featuredmedia"][0]
  ) {
    const media = post._embedded["wp:featuredmedia"][0];
    if (media.media_details && media.media_details.sizes) {
      if (media.media_details.sizes.medium_large)
        return media.media_details.sizes.medium_large.source_url;
      if (media.media_details.sizes.large)
        return media.media_details.sizes.large.source_url;
    }
    return media.source_url || defaultPlaceholder;
  }
  return defaultPlaceholder;
};

const handleImageError = (e) => {
  e.target.src = defaultPlaceholder;
};

const stripHtml = (html) => {
  if (!html) return "";
  const tmp = document.createElement("DIV");
  tmp.innerHTML = html;
  return tmp.textContent || tmp.innerText || "";
};

const formatDate = (dateString) => {
  if (!dateString) return "";
  const options = { year: "numeric", month: "long", day: "numeric" };
  const date = new Date(dateString);
  return date.toLocaleDateString("uk-UA", options);
};

onMounted(() => {
  fetchNews();
});
</script>

<style scoped>
/* ==========================================================================
   Блок: news (Секція новин коледжу)
   Методологія: БЕМ
   ========================================================================== */

.news {
  width: 100%;
  max-width: 1350px;
  margin: 0 auto;
  padding: 20px;
  font-family: system-ui, -apple-system, sans-serif;
}

.news__header {
  text-align: center;
  margin-bottom: 35px;
}

.news__title {
  font-size: 2.6rem;
  font-weight: 800;
  color: #166534;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0;
}

/* Стани завантаження та помилки */
.news__state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  text-align: center;
  border-radius: 16px;
  background-color: #f8fafc;
  gap: 15px;
}

.news__state--loading {
  color: #166534;
  font-size: 1.3rem;
  font-weight: 600;
}

.news__spinner {
  width: 48px;
  height: 48px;
  border: 4px solid #e2e8f0;
  border-top-color: #166534;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.news__state--error {
  color: #dc2626;
  font-size: 1.2rem;
}

.news__error-icon {
  font-size: 2.5rem;
}

.news__retry-btn {
  padding: 10px 24px;
  font-size: 1.1rem;
  font-weight: 700;
  background-color: #166534;
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
}

/* Сітка новин */
.news__grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 30px;
}

@media (max-width: 1024px) {
  .news__grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

/* ==========================================================================
   Блок: news-card (Картка новини)
   ========================================================================== */

.news-card {
  background: #ffffff;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
  border: 1px solid #e2e8f0;
  display: flex;
  flex-direction: column;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.news-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 35px rgba(22, 101, 52, 0.12);
}

.news-card:active {
  transform: scale(0.98);
}

.news-card__media {
  width: 100%;
  height: 200px;
  position: relative;
  background-color: #f1f5f9;
  overflow: hidden;
}

.news-card__image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.news-card__overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(to bottom, transparent 65%, rgba(0, 0, 0, 0.15) 100%);
}

.news-card__content {
  padding: 20px;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.news-card__date {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.95rem;
  font-weight: 700;
  color: #64748b;
  margin-bottom: 10px;
}

.news-card__title {
  font-size: 1.3rem;
  font-weight: 800;
  color: #1e293b;
  line-height: 1.35;
  margin-bottom: 15px;
  flex-grow: 1;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.news-card__cta {
  font-size: 1.05rem;
  font-weight: 700;
  color: #166534;
  margin-top: auto;
}

/* ==========================================================================
   Блок: news-modal (Модальне вікно новини)
   ========================================================================== */

.news-modal__overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(6, 78, 59, 0.75);
  backdrop-filter: blur(8px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.news-modal__content {
  background: #ffffff;
  border-radius: 24px;
  width: 90%;
  max-width: 1100px;
  height: 85vh;
  padding: 40px;
  position: relative;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

.news-modal__close-btn {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: #f1f5f9;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #475569;
  transition: background-color 0.2s, transform 0.1s;
}

.news-modal__close-btn:hover {
  background: #e2e8f0;
  color: #0f172a;
}

.news-modal__close-btn:active {
  background: #cbd5e1;
  transform: scale(0.92);
}

.news-modal__date {
  font-size: 1.1rem;
  font-weight: 700;
  color: #64748b;
  margin-bottom: 15px;
}

.news-modal__header {
  margin-bottom: 25px;
}

.news-modal__image {
  width: 100%;
  max-height: 420px;
  object-fit: cover;
  border-radius: 16px;
  margin-bottom: 20px;
}

.news-modal__title {
  font-size: 2.4rem;
  font-weight: 800;
  color: #0f172a;
  line-height: 1.25;
}

.news-modal__body {
  font-size: 1.25rem;
  color: #334155;
  line-height: 1.7;
}

.news-modal__text :deep(p) {
  margin-bottom: 1.2rem;
}

.news-modal__text :deep(img) {
  max-width: 100%;
  height: auto;
  border-radius: 12px;
  margin: 15px 0;
}

/* Запобігаємо відкриттю сторонніх сайтів на кіоску */
.news-modal__text :deep(a) {
  color: inherit !important;
  text-decoration: none !important;
  pointer-events: none !important;
  cursor: default !important;
}
</style>
