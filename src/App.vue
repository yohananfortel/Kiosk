<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import WellcomeToTheCollege from "./components/WellcomeToTheCollege.vue";
import VstupnaKampania from "./components/VstupnaKampania.vue"; // Підключаємо НОВИЙ файл для 2-ї сторінки

// Стан поточної сторінки (1 - Головна, 2 - Вступна кампанія)
const currentPage = ref(1);
const totalPages = 2;

// Логіка таймера простою (1 хвилина = 60000 мс)
const idleTimeout = ref(null);
const IDLE_TIME = 60000;

const resetIdleTimer = () => {
  if (idleTimeout.value) clearTimeout(idleTimeout.value);

  idleTimeout.value = setTimeout(() => {
    if (currentPage.value === 1) {
      currentPage.value = 2;
    }
  }, IDLE_TIME);
};

// Логіка свайпів для сенсорного екрана
const touchStartX = ref(0);
const touchEndX = ref(0);

const handleTouchStart = (e) => {
  touchStartX.value = e.changedTouches[0].screenX;
  resetIdleTimer();
};

const handleTouchEnd = (e) => {
  touchEndX.value = e.changedTouches[0].screenX;
  handleSwipe();
};

const handleSwipe = () => {
  const swipeDistance = touchEndX.value - touchStartX.value;
  const minSwipeDistance = 50;

  if (Math.abs(swipeDistance) > minSwipeDistance) {
    if (swipeDistance < 0 && currentPage.value < totalPages) {
      currentPage.value++;
    } else if (swipeDistance > 0 && currentPage.value > 1) {
      currentPage.value--;
    }
  }
};

onMounted(() => {
  resetIdleTimer();
  window.addEventListener("click", resetIdleTimer);
  window.addEventListener("touchstart", resetIdleTimer);
});

onUnmounted(() => {
  if (idleTimeout.value) clearTimeout(idleTimeout.value);
  window.removeEventListener("click", resetIdleTimer);
  window.removeEventListener("touchstart", resetIdleTimer);
});
</script>

<template>
  <div class="top-line"></div>

  <div class="kiosk" @touchstart="handleTouchStart" @touchend="handleTouchEnd">
    <header class="kiosk__header">
      <div class="kiosk__logo-wrapper">
        <img
          src="https://ocsnau.net/wp-content/themes/ocsnau_v3/assets/images/logo_ukr_color.png?v=2"
          alt="Логотип ОКСНАУ"
          class="kiosk__logo-img"
        />
      </div>
      <div class="kiosk__title-wrapper">
        <h1 class="kiosk__main-title">Весь коледж на одному екрані</h1>
      </div>
      <div class="kiosk__controls"></div>
    </header>

    <div class="kiosk__pages">
      <div
        class="kiosk__page-wrapper"
        :class="{
          'kiosk__page-wrapper--active': currentPage === 1,
          'kiosk__page-wrapper--left': currentPage > 1,
        }"
      >
        <WellcomeToTheCollege
          style="width: 100%; flex: 1"
        ></WellcomeToTheCollege>
      </div>

      <div
        class="kiosk__page-wrapper"
        :class="{
          'kiosk__page-wrapper--active': currentPage === 2,
          'kiosk__page-wrapper--right': currentPage < 2,
        }"
      >
        <VstupnaKampania
          style="width: 100%; flex: 1; overflow-y: auto"
        ></VstupnaKampania>
      </div>
    </div>

    <div class="kiosk__dots">
      <span
        class="kiosk__dot"
        :class="{ 'kiosk__dot--active': currentPage === 1 }"
        @click="currentPage = 1"
      ></span>
      <span
        class="kiosk__dot"
        :class="{ 'kiosk__dot--active': currentPage === 2 }"
        @click="currentPage = 2"
      ></span>
    </div>
  </div>
</template>

<style>
/* ==========================================================================
   ГЛОБАЛЬНІ СТИЛІ 
   ========================================================================== */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  user-select: none;
  -webkit-user-select: none;
}

body {
  font-family: "Roboto", Tahoma, Geneva, Verdana, sans-serif;
  background-color: #fff;
  color: #064e3b;
  overflow: hidden;
}

body {
  background: url(bg.png) no-repeat;
  background-size: cover;
  background-position-y: -35vh;
}

#app {
  background: #ffffffc4;
}

.top-line {
  height: 8px;
  background: #005f47;
  color: #fff;
}

.bold {
  font-weight: bold;
}

.button {
  padding: 8px 20px;
  background-color: #42b983;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: 0.3s;
}

/* СТИЛІ КАРТОЧОК ТА СІТКИ З WELLCOMETOTHECOLLEGE */
.tile {
  background: #ffffff94;
  border-radius: 1em;
  padding: 2rem 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  cursor: pointer;
  transition:
    transform 0.15s ease,
    box-shadow 0.15s ease;
  border: 3px solid #15803d;
}
.tile > img {
  width: 100%;
}
.tile:active {
  transform: scale(0.96);
  border-bottom-width: 2px;
  margin-top: 4px;
}
.tile-code {
  background-color: rgba(255, 255, 255, 0.2);
  padding: 0.25rem 1rem;
  border-radius: 20px;
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 1rem;
}
.tile-title {
  font-size: 3rem;
  font-weight: bold;
  margin-top: 15px;
  text-transform: uppercase;
}

.tiles-grid {
  font-family: "Roboto", sans-serif;
  display: grid;
  width: 100%;
  flex: 1 1 0%;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.5rem;
  padding: 2rem;
  align-content: start;
  padding-top: 40px;
  margin-left: auto;
  margin-right: auto;
}

.tile-card {
  font-family: "Roboto", sans-serif;
  transition:
    transform 0.15s,
    box-shadow 0.15s;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  border-radius: 1rem;
  padding: 2rem;
  text-align: center;
  color: #ffffff;
  background: #00a53f;
  min-height: 180px;
}
.flat-image {
  max-width: 150px;
  filter: invert(100%);
}

/* МОДАЛЬНІ ВІКНА (Загальні для всього додатку) */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(6, 78, 59, 0.6);
  backdrop-filter: blur(8px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}
.modal-content {
  background-color: #ffffff;
  width: 90%;
  border-radius: 24px;
  padding: 3rem;
  position: relative;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
  border-top: 12px solid #16a34a;
}
.close-btn {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  background-color: #f1f5f9;
  color: #334155;
  border: none;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  font-size: 1.2rem;
  font-weight: bold;
  cursor: pointer;
}
.close-btn:active {
  background-color: #e2e8f0;
  transform: scale(0.95);
}
.modal-header {
  margin-bottom: 2rem;
  padding-right: 8rem;
}
.modal-code {
  display: inline-block;
  background-color: #dcfce7;
  color: #166534;
  padding: 0.5rem 1.2rem;
  border-radius: 8px;
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
}
.modal-header h2 {
  font-size: 2.5rem;
  color: #064e3b;
  line-height: 1.2;
}
.modal-body p {
  font-size: 1.5rem;
  line-height: 1.6;
  color: #334155;
}

@media (max-width: 480px) {
  .tiles-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
  .tile-title {
    font-size: 1rem;
  }
}

/* ==========================================================================
   СТИЛІ ПО BEM ДЛЯ СЛАЙДЕРА (ОБОЛОНКИ)
   ========================================================================== */
.kiosk {
  height: 100vh;
  display: flex;
  flex-direction: column;
  padding: 1rem;
  position: relative;
}
.kiosk__header {
  text-align: center;
  padding-top: 1rem;
  justify-content: space-around;
  display: flex;
  align-content: center;
}
.kiosk__logo-img {
  height: 7em;
}
.kiosk__main-title {
  font-size: 3rem;
  color: #166534;
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.kiosk__pages {
  position: relative;
  flex: 1;
  width: 100%;
  overflow: hidden;
}
.kiosk__page-wrapper {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  transition:
    transform 0.5s ease-in-out,
    opacity 0.5s ease-in-out;
  opacity: 0;
  pointer-events: none;
  overflow-y: auto;
}
.kiosk__page-wrapper--active {
  transform: translateX(0);
  opacity: 1;
  pointer-events: auto;
}
.kiosk__page-wrapper--left {
  transform: translateX(-100%);
}
.kiosk__page-wrapper--right {
  transform: translateX(100%);
}

.kiosk__dots {
  display: flex;
  justify-content: center;
  gap: 15px;
  padding: 1rem 0 2.5rem 0;
  z-index: 10;
}
.kiosk__dot {
  width: 18px;
  height: 18px;
  background-color: #cbd5e1;
  border-radius: 50%;
  cursor: pointer;
  transition:
    background-color 0.3s,
    transform 0.3s;
}
.kiosk__dot--active {
  background-color: #166534;
  transform: scale(1.3);
}
</style>
