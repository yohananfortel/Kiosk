<template>
  <div class="news-container">
    <h2 class="news-title">Останні новини</h2>

    <div v-if="loading" class="loading-state">
      <div class="spinner"></div>
      <p>Завантаження новин...</p>
    </div>

    <div v-else-if="error" class="error-state">
      <svg
        class="error-icon"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
        ></path>
      </svg>
      <p>{{ error }}</p>
    </div>

    <div v-else class="news-grid">
      <div v-for="post in news" :key="post.id" class="news-card">
        <div class="news-card__image-container">
          <img
            :src="getFeaturedImage(post)"
            :alt="stripHtml(post.title.rendered)"
            class="news-card__image"
            @error="handleImageError"
          />
          <div class="news-card__overlay"></div>
        </div>
        <div class="news-card__content">
          <div class="news-card__date">
            <svg
              class="date-icon"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
              ></path>
            </svg>
            {{ formatDate(post.date) }}
          </div>
          <h3 class="news-card__title" v-html="post.title.rendered"></h3>
          <a href="#" @click.prevent="openModal(post)" class="news-card__link">
            Читати далі
            <svg
              class="arrow-icon"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M14 5l7 7m0 0l-7 7m7-7H3"
              ></path>
            </svg>
          </a>
        </div>
      </div>
    </div>

    <!-- Модальне вікно -->
    <div
      v-if="isModalOpen && selectedPost"
      class="modal-overlay"
      @click="closeModal"
    >
      <div class="modal-content" @click.stop>
        <button class="modal-close" @click="closeModal">
          <svg
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            ></path>
          </svg>
        </button>
        <div class="modal-date">
          <svg
            class="date-icon"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
            ></path>
          </svg>
          {{ formatDate(selectedPost.date) }}
        </div>
        <div class="modal-header">
          <img
            v-if="getFeaturedImage(selectedPost) !== defaultImage"
            :src="getFeaturedImage(selectedPost)"
            :alt="stripHtml(selectedPost.title.rendered)"
            class="modal-image"
          />

          <h3 v-html="selectedPost.title.rendered"></h3>
        </div>
        <div class="modal-body">
          <div
            class="modal-text"
            v-html="
              selectedPost.content?.rendered || selectedPost.excerpt?.rendered
            "
          ></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";

const news = ref([]);
const loading = ref(true);
const error = ref(null);

const isModalOpen = ref(false);
const selectedPost = ref(null);

const openModal = (post) => {
  selectedPost.value = post;
  isModalOpen.value = true;
  document.body.style.overflow = "hidden";
};

const closeModal = () => {
  isModalOpen.value = false;
  setTimeout(() => {
    selectedPost.value = null;
  }, 300); // чекаємо завершення анімації
  document.body.style.overflow = "";
};

// Очищення при знищенні компонента
onUnmounted(() => {
  document.body.style.overflow = "";
});

const defaultImage =
  "https://via.placeholder.com/400x250/e2e8f0/4a5568?text=Фото+немає";

const fetchNews = async () => {
  try {
    loading.value = true;
    error.value = null;
    const response = await fetch(
      "https://ocsnau.net/wp-json/wp/v2/news?_embed=true&per_page=6&order=desc&nocache=${new Date().getTime()}",
    );
    if (!response.ok) {
      throw new Error("Помилка при завантаженні новин з сервера");
    }
    const data = await response.json();
    news.value = data;
  } catch (err) {
    error.value =
      err.message || "Не вдалося завантажити новини. Спробуйте пізніше.";
    console.error("Помилка завантаження новин:", err);
  } finally {
    loading.value = false;
  }
};

const getFeaturedImage = (post) => {
  if (
    post._embedded &&
    post._embedded["wp:featuredmedia"] &&
    post._embedded["wp:featuredmedia"][0]
  ) {
    const media = post._embedded["wp:featuredmedia"][0];
    if (media.media_details && media.media_details.sizes) {
      // Спробуємо взяти зображення середнього або великого розміру для кращої оптимізації
      if (media.media_details.sizes.medium_large)
        return media.media_details.sizes.medium_large.source_url;
      if (media.media_details.sizes.large)
        return media.media_details.sizes.large.source_url;
    }
    return media.source_url;
  }
  return defaultImage;
};

const handleImageError = (e) => {
  e.target.src = defaultImage;
};

const stripHtml = (html) => {
  const tmp = document.createElement("DIV");
  tmp.innerHTML = html;
  return tmp.textContent || tmp.innerText || "";
};

const formatDate = (dateString) => {
  const options = { year: "numeric", month: "long", day: "numeric" };
  const date = new Date(dateString);
  return date.toLocaleDateString("uk-UA", options);
};

onMounted(() => {
  fetchNews();
});
</script>

<style scoped>
.news-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
  font-family:
    "Inter",
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    Roboto,
    Oxygen,
    Ubuntu,
    Cantarell,
    sans-serif;
}

.news-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: #1a202c;
  margin-bottom: 3rem;
  text-align: center;
  position: relative;
}

.news-title::after {
  content: "";
  display: block;
  width: 60px;
  height: 4px;
  background: #3182ce;
  margin: 10px auto 0;
  border-radius: 2px;
}

/* Стани завантаження та помилки */
.loading-state,
.error-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  text-align: center;
  border-radius: 12px;
  background-color: #f7fafc;
}

.loading-state p {
  margin-top: 1rem;
  font-size: 1.2rem;
  color: #4a5568;
  font-weight: 500;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #e2e8f0;
  border-top: 4px solid #3182ce;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.error-state {
  background-color: #fff5f5;
}

.error-icon {
  width: 48px;
  height: 48px;
  color: #e53e3e;
  margin-bottom: 1rem;
}

.error-state p {
  color: #c53030;
  font-size: 1.1rem;
  font-weight: 500;
}

/* Сітка новин */
.news-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 2.5rem;
}

/* Картка новини */
.news-card {
  background: #ffffff;
  border-radius: 16px;
  overflow: hidden;
  box-shadow:
    0 4px 6px -1px rgba(0, 0, 0, 0.05),
    0 2px 4px -1px rgba(0, 0, 0, 0.03);
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  border: 1px solid #edf2f7;
  position: relative;
  z-index: 1;
}

.news-card:hover {
  transform: translateY(-8px);
  box-shadow:
    0 20px 25px -5px rgba(0, 0, 0, 0.1),
    0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

.news-card__image-container {
  width: 100%;
  height: 220px;
  overflow: hidden;
  position: relative;
  background-color: #e2e8f0;
}

.news-card__image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.news-card:hover .news-card__image {
  transform: scale(1.08);
}

.news-card__overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    to bottom,
    transparent 60%,
    rgba(0, 0, 0, 0.1) 100%
  );
  pointer-events: none;
}

.news-card__content {
  padding: 1.75rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.news-card__date {
  display: flex;
  align-items: center;
  font-size: 0.85rem;
  color: #718096;
  margin-bottom: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.date-icon {
  width: 16px;
  height: 16px;
  margin-right: 6px;
  color: #a0aec0;
}

.news-card__title {
  font-size: 1.35rem;
  font-weight: 700;
  color: #1a202c;
  margin: 0 0 1rem 0;
  line-height: 1.3;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.news-card__title :deep(*) {
  color: inherit;
  text-decoration: none;
}

.news-card__excerpt {
  font-size: 0.95rem;
  color: #4a5568;
  line-height: 1.6;
  margin-bottom: 1.5rem;
  flex-grow: 1;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.news-card__excerpt :deep(p) {
  margin: 0;
}

.news-card__link {
  align-self: flex-start;
  display: inline-flex;
  align-items: center;
  padding: 0.6rem 1.2rem;
  background-color: #f7fafc;
  color: #3182ce;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.2s ease;
  border: 1px solid #e2e8f0;
}

.news-card__link:hover {
  background-color: #3182ce;
  color: white;
  border-color: #3182ce;
}

.arrow-icon {
  width: 16px;
  height: 16px;
  margin-left: 8px;
  transition: transform 0.2s ease;
}

.news-card__link:hover .arrow-icon {
  transform: translateX(4px);
}

@media (max-width: 768px) {
  .news-grid {
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.5rem;
  }

  .news-title {
    font-size: 2rem;
    margin-bottom: 2rem;
  }
}

/* Модальне вікно */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 20px;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.modal-content {
  background: white;
  border-radius: 16px;
  width: 100%;
  max-width: 80vw;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  display: flex;
  flex-direction: column;
  animation: slideUp 0.3s ease;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

@keyframes slideUp {
  from {
    transform: translateY(20px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.modal-close {
  position: absolute;
  top: 15px;
  right: 15px;
  background: #f7fafc;
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: #4a5568;
  transition: all 0.2s ease;
  z-index: 10;
}

.modal-close:hover {
  background: #edf2f7;
  color: #1a202c;
  transform: scale(1.05);
}

.modal-close svg {
  width: 24px;
  height: 24px;
}

.modal-header {
  display: flex;
  padding: 30px 40px 20px;
  border-bottom: 1px solid #edf2f7;
  flex-wrap: nowrap;
  flex-direction: row;
  justify-content: center;
  align-content: center;
  align-items: flex-start;
}

.modal-header h3 {
  font-size: 3em;
  font-weight: 800;
  color: #1a202c;
  margin: 0 0 10px 0;
  line-height: 1.3;
  padding-right: 40px;
}

.modal-date {
  display: flex;
  align-items: center;
  font-size: 0.9rem;
  color: #718096;
  font-weight: 600;
  width: 100%;
}

.modal-body {
  padding: 30px 40px;
}

.modal-image {
  width: auto;
  max-height: 400px;
  /* object-fit: scale-down; */
  border-radius: 12px;
  margin-bottom: 25px;
  margin-right: 20px;
}

.modal-text {
  font-size: 1.05rem;
  color: #2d3748;
  line-height: 1.7;
  word-wrap: break-word;
}

.modal-text :deep(p) {
  margin-bottom: 1.5rem;
}

.modal-text :deep(img) {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  display: block !important;
  margin: 1.5rem auto !important;
}

.modal-text :deep(a) {
  color: #3182ce;
  text-decoration: underline;
}

.modal-text :deep(iframe) {
  max-width: 100%;
}

.modal-text :deep(figure) {
  margin: 0;
}

@media (max-width: 640px) {
  .modal-overlay {
    padding: 10px;
  }
  .modal-header {
    padding: 20px 20px 15px;
  }
  .modal-header h3 {
    font-size: 3em;
  }
  .modal-body {
    padding: 20px;
  }
}
</style>
