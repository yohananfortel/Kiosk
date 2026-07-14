<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import WellcomeToTheCollege from "./components/WellcomeToTheCollege.vue";
import VstupnaKampania from "./components/VstupnaKampania.vue";

const currentPage = ref(1);
const totalPages = 2;

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
    <!-- Додано динамічний клас: якщо сторінка 2, шапка стискається -->
    <header
      class="kiosk__header"
      :class="{ 'kiosk__header--compact': currentPage === 2 }"
    >
      <div class="kiosk__logo-wrapper">
        <img
          src="https://ocsnau.net/wp-content/themes/ocsnau_v3/assets/images/logo_ukr_color.png?v=2"
          alt="Логотип ОКСНАУ"
          class="kiosk__logo-img"
        />
      </div>

      <Transition name="fade">
        <div v-show="currentPage === 1" class="kiosk__title-wrapper main-hero">
          <h1 class="main-hero__title">
            Весь коледж <br />
            <span class="main-hero__highlight">на одному екрані</span>
          </h1>
        </div>
      </Transition>
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
  position: relative;
  width: 100%;
  min-height: 180px; /* Висота для першої сторінки */
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 10px;
  transition: min-height 0.4s ease; /* Плавна зміна висоти */
}

/* Стиснута шапка для другої сторінки */
.kiosk__header--compact {
  min-height: 90px; /* Зменшуємо висоту, підтягуючи контент вгору */
}

.kiosk__logo-wrapper {
  position: absolute;
  left: 40px;
  top: 15px;
  z-index: 10;
}

.kiosk__logo-img {
  height: 7em;
}

/* ==========================================================================
   НОВІ СТИЛІ ГОЛОВНОГО ЗАГОЛОВКУ
   ========================================================================== */
.main-hero {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.main-hero__title {
  font-size: 4rem;
  font-weight: 900;
  color: #1e293b;
  line-height: 1.1;
  margin: 0;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.main-hero__highlight {
  color: #166534;
  text-shadow: 0 10px 25px rgba(22, 101, 52, 0.15);
}

/* Анімація зникнення тексту */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* ==========================================================================
   СТИЛІ КАРТОЧОК ТА ІНШОГО
   ========================================================================== */
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
</style>
