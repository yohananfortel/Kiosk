<template>
  <div class="specialties">
    <header class="specialties__header">
      <h1 class="specialties__title">Спеціальності нашого закладу</h1>
      <p class="specialties__subtitle">
        Оберіть спеціальність для отримання детальної інформації
      </p>
    </header>

    <div v-if="loading && specialties.length === 0" class="specialties__state specialties__state--loading">
      <div class="specialties__spinner"></div>
      <p>Завантаження спеціальностей...</p>
    </div>

    <div v-else-if="error && specialties.length === 0" class="specialties__state specialties__state--error">
      <svg viewBox="0 0 24 24" width="42" height="42" fill="none" stroke="#dc2626" stroke-width="2">
        <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z" />
        <line x1="12" y1="9" x2="12" y2="13" />
        <line x1="12" y1="17" x2="12.01" y2="17" />
      </svg>
      <p>{{ error }}</p>
      <button class="specialties__retry-btn" @click="fetchSpecialties(true)">Спробувати знову</button>
    </div>

    <main v-else class="specialties__grid">
      <div
        v-for="item in specialties"
        :key="item.id"
        class="specialty-card"
        @click="openModal(item)"
      >
        <div class="specialty-card__media">
          <img
            v-if="item.thumbnail"
            :src="item.thumbnail"
            :alt="item.title || item.name"
            class="specialty-card__image"
          />
          <div v-else class="specialty-card__placeholder">
            <svg viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="#166534" stroke-width="2">
              <path d="M22 10v6M2 10l10-5 10 5-10 5z" />
              <path d="M6 12v5c3 3 9 3 12 0v-5" />
            </svg>
          </div>
        </div>

        <div class="specialty-card__content">
          <h3 class="specialty-card__title">{{ item.title || item.name }}</h3>
        </div>
      </div>
    </main>

    <!-- Модальне вікно спеціальності -->
    <Teleport to="body">
      <Transition name="fade">
        <div
          v-if="selectedSpecialty"
          class="specialty-modal__overlay"
          @click.self="closeModal"
        >
          <div class="specialty-modal__content">
            <button class="specialty-modal__close-btn" @click="closeModal">
              &times;
            </button>

            <header class="specialty-modal__header">
              <h2 class="specialty-modal__title">
                {{ selectedSpecialty.name || selectedSpecialty.title }}
              </h2>
            </header>

            <div class="specialty-modal__body">
              <div class="specialty-modal__meta">
                <span class="specialty-modal__meta-icon">
                  <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#166534" stroke-width="2">
                    <circle cx="12" cy="12" r="10" />
                    <polyline points="12 6 12 12 16 14" />
                  </svg>
                </span>
                <div class="specialty-modal__meta-info">
                  <span class="specialty-modal__meta-label">Термін навчання:</span>
                  <span class="specialty-modal__meta-value">
                    {{ selectedSpecialty.l || selectedSpecialty.duration || selectedSpecialty.term || "Згідно з освітньою програмою" }}
                  </span>
                </div>
              </div>

              <div class="specialty-modal__desc-block">
                <h4 class="specialty-modal__desc-title">Про спеціальність:</h4>
                <p class="specialty-modal__desc-text">
                  {{ selectedSpecialty.description || "Інформація про спеціальність уточнюється у приймальній комісії." }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { fetchWithCache, getCachedData } from "../utils/cache";

const selectedSpecialty = ref(null);
const specialties = ref([]);
const loading = ref(true);
const error = ref(null);

const fetchSpecialties = async (forceRefresh = false) => {
  const url = "https://ocsnau.net/wp-json/spa/v1/specialties";
  try {
    loading.value = true;
    error.value = null;

    if (!forceRefresh) {
      const cached = getCachedData(url, true);
      if (cached && Array.isArray(cached) && cached.length > 0) {
        specialties.value = cached;
      }
    }

    const data = await fetchWithCache(url, {}, 1000 * 60 * 60 * 24);
    if (Array.isArray(data)) {
      specialties.value = data;
    }
  } catch (err) {
    if (specialties.value.length === 0) {
      error.value = "Не вдалося завантажити перелік спеціальностей.";
    }
    console.error("[Speciality] Помилка завантаження:", err);
  } finally {
    loading.value = false;
  }
};

const openModal = (specialty) => {
  selectedSpecialty.value = specialty;
};

const closeModal = () => {
  selectedSpecialty.value = null;
};

onMounted(() => {
  fetchSpecialties();
});
</script>

<style scoped>
/* ==========================================================================
   Блок: specialties (Каталог спеціальностей)
   Методологія: БЕМ
   ========================================================================== */

.specialties {
  padding: 10px;
  width: 100%;
  font-family: system-ui, -apple-system, sans-serif;
}

.specialties__header {
  margin-bottom: 35px;
  text-align: center;
}

.specialties__title {
  font-size: 2.6rem;
  font-weight: 800;
  color: #166534;
  text-transform: uppercase;
  margin: 0 0 10px 0;
  letter-spacing: 1px;
}

.specialties__subtitle {
  font-size: 1.3rem;
  color: #64748b;
  margin: 0;
}

.specialties__state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  text-align: center;
  gap: 15px;
  border-radius: 16px;
  background-color: #f8fafc;
}

.specialties__state--loading {
  color: #166534;
  font-size: 1.3rem;
  font-weight: 600;
}

.specialties__spinner {
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

.specialties__state--error {
  color: #dc2626;
  font-size: 1.2rem;
}

.specialties__error-icon {
  font-size: 2.5rem;
}

.specialties__retry-btn {
  padding: 10px 24px;
  font-size: 1.1rem;
  font-weight: 700;
  background-color: #166534;
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
}

/* ==========================================================================
   Сітка та картка спеціальності
   ========================================================================== */

.specialties__grid {
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
  justify-content: center;
  align-items: stretch;
  max-width: 1400px;
  margin: 0 auto;
}

.specialty-card {
  width: 320px;
  height: 380px;
  background: #ffffff;
  border-radius: 24px;
  display: flex;
  flex-direction: column;
  cursor: pointer;
  overflow: hidden;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
  border: 1px solid #e2e8f0;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.specialty-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 25px 45px rgba(22, 101, 52, 0.15);
}

.specialty-card:active {
  transform: scale(0.97);
}

.specialty-card__media {
  width: 100%;
  height: 220px;
  background-color: #f1f5f9;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.specialty-card__image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.specialty-card__placeholder {
  font-size: 4rem;
}

.specialty-card__content {
  padding: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 1;
  text-align: center;
}

.specialty-card__title {
  font-size: 1.4rem;
  font-weight: 800;
  color: #1e293b;
  line-height: 1.3;
}

/* ==========================================================================
   Блок: specialty-modal (Модальне вікно опису спеціальності)
   ========================================================================== */

.specialty-modal__overlay {
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
  z-index: 2000;
}

.specialty-modal__content {
  background: #ffffff;
  border-radius: 24px;
  width: 90%;
  max-width: 900px;
  max-height: 80vh;
  padding: 40px;
  position: relative;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

.specialty-modal__close-btn {
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
  transition: all 0.15s ease;
}

.specialty-modal__close-btn:hover {
  background: #e2e8f0;
  color: #0f172a;
}

.specialty-modal__close-btn:active {
  background: #cbd5e1;
  transform: scale(0.92);
}

.specialty-modal__header {
  margin-bottom: 25px;
  padding-right: 40px;
}

.specialty-modal__title {
  font-size: 2.2rem;
  font-weight: 800;
  color: #166534;
  line-height: 1.25;
}

.specialty-modal__meta {
  display: flex;
  align-items: center;
  gap: 15px;
  background: #f0fdf4;
  padding: 16px 20px;
  border-radius: 16px;
  border: 1px solid #bbf7d0;
  margin-bottom: 25px;
}

.specialty-modal__meta-icon {
  font-size: 2rem;
}

.specialty-modal__meta-label {
  display: block;
  font-size: 0.95rem;
  font-weight: 700;
  color: #166534;
  text-transform: uppercase;
}

.specialty-modal__meta-value {
  font-size: 1.25rem;
  font-weight: 800;
  color: #0f172a;
}

.specialty-modal__desc-title {
  font-size: 1.3rem;
  font-weight: 800;
  color: #1e293b;
  margin-bottom: 12px;
}

.specialty-modal__desc-text {
  font-size: 1.2rem;
  color: #475569;
  line-height: 1.65;
}
</style>
