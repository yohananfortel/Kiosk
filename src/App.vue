<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import Schedule from "./components/Schedule.vue";
import WellcomeToTheCollege from "./components/WellcomeToTheCollege.vue";
import VstupnaKampania from "./components/VstupnaKampania.vue";

const currentPage = ref(1);
const totalPages = 3;

const welcomeRef = ref(null);
const campaignRef = ref(null);

const idleTimeout = ref(null);
const IDLE_TIME = 90000; // 90 секунд бездіяльності до повернення на головну

const resetIdleTimer = () => {
  if (idleTimeout.value) clearTimeout(idleTimeout.value);

  idleTimeout.value = setTimeout(() => {
    // При таймауті:
    // 1. Повертаємося на головний екран
    currentPage.value = 1;
    // 2. Закриваємо відкриті модалки
    if (welcomeRef.value?.closeModal) welcomeRef.value.closeModal();
    if (campaignRef.value?.closeModal) campaignRef.value.closeModal();
  }, IDLE_TIME);
};

const touchStartX = ref(0);
const touchStartY = ref(0);
const touchEndX = ref(0);
const touchEndY = ref(0);

const isAnyModalOpen = () => {
  return Boolean(welcomeRef.value?.isModalOpen || campaignRef.value?.isModalOpen);
};

const handleTouchStart = (e) => {
  touchStartX.value = e.changedTouches[0].screenX;
  touchStartY.value = e.changedTouches[0].screenY;
  resetIdleTimer();
};

const handleTouchEnd = (e) => {
  touchEndX.value = e.changedTouches[0].screenX;
  touchEndY.value = e.changedTouches[0].screenY;
  handleSwipe();
};

const handleSwipe = () => {
  // Не перемикаємо головні сторінки, якщо користувач взаємодіє з модальним вікном
  if (isAnyModalOpen()) return;

  const diffX = touchEndX.value - touchStartX.value;
  const diffY = touchEndY.value - touchStartY.value;
  const minSwipeDistance = 60;

  // Горизонтальний свайп має переважати вертикальний рух
  if (Math.abs(diffX) > minSwipeDistance && Math.abs(diffX) > Math.abs(diffY) * 1.5) {
    if (diffX < 0 && currentPage.value < totalPages) {
      currentPage.value++;
    } else if (diffX > 0 && currentPage.value > 1) {
      currentPage.value--;
    }
  }
};

const handleLogoError = (e) => {
  e.target.src = `${import.meta.env.BASE_URL}img/college.png`;
};

// Захист кіоску: повна заборона відкриття будь-яких посилань та переходу на сторонні сайти
const blockAllLinks = (e) => {
  const target = e.target?.closest?.("a");
  if (target) {
    e.preventDefault();
    e.stopPropagation();
  }
};

onMounted(() => {
  resetIdleTimer();
  window.addEventListener("pointerdown", resetIdleTimer, { passive: true });
  window.addEventListener("touchstart", resetIdleTimer, { passive: true });
  window.addEventListener("click", blockAllLinks, { capture: true });
  window.addEventListener("auxclick", blockAllLinks, { capture: true });
});

onUnmounted(() => {
  if (idleTimeout.value) clearTimeout(idleTimeout.value);
  window.removeEventListener("pointerdown", resetIdleTimer);
  window.removeEventListener("touchstart", resetIdleTimer);
  window.removeEventListener("click", blockAllLinks, { capture: true });
  window.removeEventListener("auxclick", blockAllLinks, { capture: true });
});
</script>

<template>
  <div class="kiosk-bar"></div>

  <div class="kiosk" @touchstart="handleTouchStart" @touchend="handleTouchEnd">
    <header
      class="kiosk__header"
      :class="{ 'kiosk__header--compact': currentPage !== 2 }"
    >
      <div class="kiosk__logo-box">
        <img
          src="https://ocsnau.net/wp-content/themes/ocsnau_v3/assets/images/logo_ukr_color.png?v=2"
          alt="Логотип ОКСНАУ"
          class="kiosk__logo-image"
          @error="handleLogoError"
        />
      </div>

      <Transition name="fade">
        <div v-if="currentPage === 2" class="kiosk__hero">
          <h1 class="kiosk__hero-title">
            <span class="kiosk__hero-highlight">Весь коледж на одному екрані</span>
          </h1>
        </div>
      </Transition>
    </header>

    <div class="kiosk__pages">
      <div
        class="kiosk__page"
        :class="{
          'kiosk__page--active': currentPage === 1,
          'kiosk__page--left': currentPage > 1,
        }"
      >
        <Schedule class="kiosk__page-content" />
      </div>

      <div
        class="kiosk__page"
        :class="{
          'kiosk__page--active': currentPage === 2,
          'kiosk__page--left': currentPage > 2,
          'kiosk__page--right': currentPage < 2,
        }"
      >
        <WellcomeToTheCollege ref="welcomeRef" class="kiosk__page-content" />
      </div>

      <div
        class="kiosk__page"
        :class="{
          'kiosk__page--active': currentPage === 3,
          'kiosk__page--right': currentPage < 3,
        }"
      >
        <VstupnaKampania ref="campaignRef" class="kiosk__page-content" />
      </div>
    </div>

    <div class="kiosk__dots">
      <button
        class="kiosk__dot"
        :class="{ 'kiosk__dot--active': currentPage === 1 }"
        aria-label="Розклад"
        @click="currentPage = 1"
      ></button>
      <button
        class="kiosk__dot"
        :class="{ 'kiosk__dot--active': currentPage === 2 }"
        aria-label="Головна сторінка"
        @click="currentPage = 2"
      ></button>
      <button
        class="kiosk__dot"
        :class="{ 'kiosk__dot--active': currentPage === 3 }"
        aria-label="Вступна кампанія"
        @click="currentPage = 3"
      ></button>
    </div>
  </div>
</template>

<style>
/* ==========================================================================
   ГЛОБАЛЬНІ СТИЛІ КІОСКУ
   ========================================================================== */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  user-select: none;
  -webkit-user-select: none;
  -webkit-touch-callout: none;
  -webkit-tap-highlight-color: transparent;
}

/* Кастомний сенсорний скролбар для сенсорних панелей / кіосків */
::-webkit-scrollbar {
  width: 10px;
  height: 10px;
}
::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 8px;
}
::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 8px;
  border: 2px solid #f1f5f9;
}
::-webkit-scrollbar-thumb:hover,
::-webkit-scrollbar-thumb:active {
  background: #166534;
}

html,
body {
  width: 100vw;
  height: 100vh;
  overflow: hidden !important;
  font-family: "Roboto", Tahoma, Geneva, Verdana, sans-serif;
  background-color: #ffffff;
  color: #064e3b;
  -webkit-overflow-scrolling: touch;
}

body {
  background: url('@/assets/bg.png') no-repeat center center fixed;
  background-size: cover;
}

/* Повна заборона переходу за посиланнями для автономного кіоску */
a,
a:visited,
a:hover,
a:active,
a:focus {
  pointer-events: none !important;
  cursor: default !important;
  text-decoration: none !important;
  color: inherit !important;
}

#app {
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.88);
  backdrop-filter: blur(2px);
  overflow: hidden;
}

.kiosk-bar {
  height: 8px;
  background: #005f47;
  width: 100%;
}

/* ==========================================================================
   Блок: kiosk (Оболонка терміналу)
   Методологія: БЕМ
   ========================================================================== */

.kiosk {
  height: calc(100vh - 8px);
  display: flex;
  flex-direction: column;
  padding: 1.2rem;
  position: relative;
  overflow: hidden;
}

.kiosk__header {
  width: 100%;
  display: grid;
  grid-template-columns: 220px 1fr;
  align-items: center;
  transition: all 0.3s ease;
}

.kiosk__header--compact {
  height: 90px;
}

.kiosk__logo-box {
  display: flex;
  align-items: center;
}

.kiosk__logo-image {
  height: 85px;
  max-width: 100%;
  object-fit: contain;
  transition: height 0.3s ease;
}

.kiosk__hero {
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

.kiosk__hero-title {
  font-size: 2.8rem;
  font-weight: 900;
  margin: 0;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.kiosk__hero-highlight {
  color: #166534;
  text-shadow: 0 4px 15px rgba(22, 101, 52, 0.12);
}

/* ==========================================================================
   Сторінки кіоску (Слайдер)
   ========================================================================== */

.kiosk__pages {
  position: relative;
  flex: 1;
  width: 100%;
  overflow: hidden;
  margin-top: 10px;
}

.kiosk__page {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  transition: transform 0.45s ease-in-out, opacity 0.45s ease-in-out;
  opacity: 0;
  pointer-events: none;
  overflow-y: auto;
}

.kiosk__page--active {
  transform: translateX(0);
  opacity: 1;
  pointer-events: auto;
}

.kiosk__page--left {
  transform: translateX(-100%);
}

.kiosk__page--right {
  transform: translateX(100%);
}

.kiosk__page-content {
  width: 100%;
  flex: 1;
}

/* ==========================================================================
   Елемент: kiosk__dots (Пагінація слайдера)
   ========================================================================== */

.kiosk__dots {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 12px;
  padding: 0.8rem 0 1.2rem 0;
  z-index: 10;
}

.kiosk__dot {
  width: 48px;
  height: 48px;
  background: transparent;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
}

.kiosk__dot::after {
  content: "";
  display: block;
  width: 18px;
  height: 18px;
  background-color: #cbd5e1;
  border-radius: 50%;
  transition: all 0.25s ease;
}

.kiosk__dot--active::after {
  background-color: #166534;
  width: 42px;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(22, 101, 52, 0.25);
}

/* Загальні анімації появи */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.25s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>

