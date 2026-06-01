<script setup>
import { ref, onMounted } from "vue";

const selectedSpecialty = ref(null);
const specialties = ref([]);
const loading = ref(true);
const error = ref(null);

const fetchSpecialties = async () => {
  try {
    const response = await fetch("//ocsnau.net/wp-json/spa/v1/specialties");

    if (!response.ok) {
      throw new Error("Помилка при завантаженні даних");
    }

    specialties.value = await response.json();
    console.log("Завантажені спеціальності:", specialties.value);
  } catch (err) {
    error.value = err.message;
    console.error("Помилка при завантаженні спеціальностей:", err);
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

<template>
  <div class="specialties">
    <header class="specialties__header">
      <h1 class="specialties__main-title">Спеціальності нашого закладу</h1>
      <p class="specialties__subtitle">
        Оберіть спеціальність для отримання детальної інформації
      </p>
    </header>

    <div v-if="loading" class="specialties__loading">
      <div class="specialties__spinner"></div>
      <p class="specialties__loading-text">Завантаження спеціальностей...</p>
    </div>

    <div v-else-if="error" class="specialties__error">
      <span class="specialties__error-icon">⚠️</span>
      <p class="specialties__error-text">{{ error }}</p>
    </div>

    <main v-else class="specialties__grid">
      <div
        v-for="item in specialties"
        :key="item.id"
        class="specialty-card"
        @click="openModal(item)"
      >
        <div class="specialty-card__image-container">
          <img
            v-if="item.thumbnail"
            :src="item.thumbnail"
            alt="Specialty image"
            class="specialty-card__image"
          />
          <div v-else class="specialty-card__placeholder">🎓</div>
        </div>

        <div class="specialty-card__content">
          <h3 class="specialty-card__title">{{ item.title || item.name }}</h3>
        </div>
      </div>
    </main>

    <Teleport to="body">
      <Transition name="submodal-fade">
        <div
          v-if="selectedSpecialty"
          class="specialty-modal"
          @click.self="closeModal"
        >
          <div class="specialty-modal__content">
            <button class="specialty-modal__close-btn" @click="closeModal">
              ✕ Закрити
            </button>

            <header class="specialty-modal__header">
              <h2 class="specialty-modal__title">
                {{ selectedSpecialty.name || selectedSpecialty.title }}
              </h2>
            </header>

            <div class="specialty-modal__body">
              <div class="specialty-detail">
                <div class="specialty-detail__meta">
                  <span class="specialty-detail__meta-icon">⏱️</span>
                  <div class="specialty-detail__meta-info">
                    <span class="specialty-detail__meta-label"
                      >Термін навчання</span
                    >
                    <span class="specialty-detail__meta-value">{{
                      selectedSpecialty.l || "Не вказано"
                    }}</span>
                  </div>
                </div>

                <div class="specialty-detail__description-block">
                  <h4 class="specialty-detail__description-title">
                    Про спеціальність
                  </h4>
                  <p class="specialty-detail__description-text">
                    {{ selectedSpecialty.description }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<style scoped>
/* =========================================
   Блок: specialties
   ========================================= */
.specialties {
  padding: 10px;
}

.specialties__header {
  margin-bottom: 40px;
  text-align: center; /* Центруємо заголовок для повної симетрії */
}

.specialties__main-title {
  font-size: 3rem;
  font-weight: 800;
  color: #166534;
  text-transform: uppercase;
  margin: 0 0 10px 0;
  letter-spacing: 1px;
}

.specialties__subtitle {
  font-size: 1.4rem;
  color: #64748b;
  margin: 0;
}

/* =========================================
   Сітка карток (Ідеальна симетрія)
   ========================================= */
.specialties__grid {
  display: flex;
  flex-wrap: wrap; /* Дозволяє переносити картки */
  gap: 40px; /* Однаковий відступ між усіма картками */
  justify-content: center; /* Рівно по центру завжди! */
  align-items: stretch;
  max-width: 1400px;
  margin: 0 auto;
}

/* =========================================
   Картки спеціальностей (Преміум стиль)
   ========================================= */
.specialty-card {
  width: 320px; /* Суворо фіксована ширина */
  height: 380px; /* Суворо фіксована висота */
  background: #ffffff;
  border-radius: 24px;
  display: flex;
  flex-direction: column;
  cursor: pointer;
  overflow: hidden; /* Щоб картинка не вилазила за рамки */
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08); /* М'яка тінь */
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
  position: relative;
}

/* Анімація підстрибування */
.specialty-card:hover {
  transform: translateY(-12px);
  box-shadow: 0 25px 45px rgba(22, 101, 52, 0.15); /* Тінь з легким зеленим відтінком */
}

.specialty-card:active {
  transform: scale(0.96);
}

/* Блок з картинкою зверху */
.specialty-card__image-container {
  width: 100%;
  height: 200px; /* Більше половини картки — це яскраве фото */
  background: #f1f5f9;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  border-bottom: 4px solid #00a53f; /* Стильна зелена лінія розділення */
}

.specialty-card__image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease; /* Плавний зум */
}

/* Ефект зуму картинки при наведенні на картку */
.specialty-card:hover .specialty-card__image {
  transform: scale(1.1);
}

.specialty-card__placeholder {
  font-size: 5rem;
}

/* Текстовий блок знизу */
.specialty-card__content {
  padding: 20px;
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #ffffff;
}

.specialty-card__title {
  font-size: 1.4rem;
  font-weight: 800;
  color: #1e293b;
  text-align: center;
  line-height: 1.3;
  margin: 0;

  /* Захист, якщо назва надто довга (обріже трьома крапками) */
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* =========================================
   Індикатори завантаження та помилки
   ========================================= */
.specialties__loading,
.specialties__error {
  text-align: center;
  padding: 50px;
}

.specialties__spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #00a53f;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
  margin: 0 auto 20px;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.specialties__loading-text {
  font-size: 1.5rem;
  color: #64748b;
}

.specialties__error-icon {
  font-size: 4rem;
  display: block;
  margin-bottom: 10px;
}

.specialties__error-text {
  font-size: 1.4rem;
  color: #ef4444;
  font-weight: 600;
}

/* =========================================
   Внутрішнє модальне вікно (Стилізоване)
   ========================================= */
.specialty-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(15, 23, 42, 0.65);
  backdrop-filter: blur(10px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2000;
}

.specialty-modal__content {
  background-color: #ffffff;
  width: 85%;
  max-width: 1000px;
  max-height: 85vh;
  border-radius: 30px;
  padding: 50px;
  position: relative;
  box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.4);
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

.specialty-modal__close-btn {
  position: absolute;
  top: 25px;
  right: 25px;
  background: #f1f5f9;
  border: none;
  border-radius: 30px;
  padding: 12px 24px;
  font-size: 1.2rem;
  font-weight: 700;
  color: #475569;
  cursor: pointer;
  transition: all 0.2s ease;
}

.specialty-modal__close-btn:hover {
  background: #ef4444;
  color: #ffffff;
  transform: scale(1.05);
}

.specialty-modal__header {
  margin-bottom: 30px;
  border-bottom: 2px solid #f1f5f9;
  padding-bottom: 20px;
}

.specialty-modal__title {
  font-size: 2.5rem;
  font-weight: 800;
  color: #1e293b;
  line-height: 1.2;
  margin: 0;
  padding-right: 150px;
}

.specialty-detail {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.specialty-detail__meta {
  display: flex;
  align-items: center;
  gap: 20px;
  background: #f0fdf4;
  border-left: 8px solid #00a53f;
  padding: 20px 30px;
  border-radius: 0 20px 20px 0;
}

.specialty-detail__meta-icon {
  font-size: 2.5rem;
}

.specialty-detail__meta-info {
  display: flex;
  flex-direction: column;
}

.specialty-detail__meta-label {
  font-size: 1rem;
  font-weight: 700;
  color: #166534;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.specialty-detail__meta-value {
  font-size: 1.6rem;
  font-weight: 800;
  color: #14532d;
  margin-top: 4px;
}

.specialty-detail__description-block {
  background: #f8fafc;
  padding: 35px;
  border-radius: 25px;
  border: 1px solid #e2e8f0;
}

.specialty-detail__description-title {
  font-weight: 700;
  color: #334155;
  margin: 0 0 20px 0;
  text-transform: uppercase;
  font-size: 1.3rem;
  letter-spacing: 0.5px;
}

.specialty-detail__description-text {
  font-size: 1.4rem;
  line-height: 1.7;
  color: #334155;
  margin: 0;
  white-space: pre-line;
  text-align: justify;
}

.submodal-fade-enter-active,
.submodal-fade-leave-active {
  transition: opacity 0.3s ease;
}
.submodal-fade-enter-from,
.submodal-fade-leave-to {
  opacity: 0;
}
</style>
