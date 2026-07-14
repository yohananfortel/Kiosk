<template>
  <div class="student-menu">
    <div class="student-menu__grid">
      <div
        v-for="item in menuItemsStudent"
        :key="item.id"
        class="student-menu__card"
        :style="{ backgroundColor: item.color || '#00a53f' }"
        @click="openModal(item)"
      >
        <div class="student-menu__icon-wrapper">
          <img
            v-if="item.image"
            :src="item.image"
            :alt="item.title"
            class="student-menu__image"
          />
        </div>
        <h3 class="student-menu__title">{{ item.title }}</h3>
      </div>
    </div>

    <Transition name="fade">
      <div
        v-if="isModalOpen"
        class="student-modal__overlay"
        @click.self="closeModal"
      >
        <div class="student-modal__content">
          <button class="student-modal__close-btn" @click="closeModal">
            &times;
          </button>

          <component :is="activeComponent" v-if="activeComponent" />

          <div v-else class="student-modal__empty-state">
            <h2 class="student-modal__empty-title">
              Розділ "{{ currentTitle }}" знаходиться у розробці
            </h2>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, shallowRef } from "vue";
import BuildSchema from "./BuildSchema.vue";
import Schedule from "./Shedule.vue";

const isModalOpen = ref(false);
const activeComponent = shallowRef(null);
const currentTitle = ref("");

// Дані збережено, кольори уніфіковано під єдиний зелений стиль
const menuItemsStudent = ref([
  {
    id: 1,
    title: "Карта аудиторій",
    color: "#00a53f",
    component: BuildSchema,
    image: "img/route.png",
  },
  {
    id: 2,
    title: "Розклад занять",
    color: "#00a53f",
    component: Schedule,
    image: "img/roskladzanat.png",
  },
]);

const openModal = (item) => {
  currentTitle.value = item.title;
  activeComponent.value = item.component || null;
  isModalOpen.value = true;
  document.body.style.overflow = "hidden";
};

const closeModal = () => {
  isModalOpen.value = false;
  activeComponent.value = null;
  document.body.style.overflow = "auto";
};
</script>

<style scoped>
/* =========================================
   Блок: student-menu (Меню студента)
   Методологія: БЕМ + Абсолютна симетрія
   ========================================= */

.student-menu {
  width: 100%;
  min-height: 70vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  box-sizing: border-box;
}

/* Елемент: Контейнер сітки карток */
.student-menu__grid {
  display: flex;
  flex-wrap: wrap;
  gap: 50px; /* Великий красивий простір між двома картами */
  justify-content: center; /* Рівняє їх строго по центру екрана */
  align-items: center;
  width: 100%;
  max-width: 1000px;
  margin: 0 auto;
}

/* Елемент: Велика квадратна картка (Стиль 1 та 2 сторінок) */
.student-menu__card {
  width: 350px;
  height: 350px;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  cursor: pointer;
  padding: 30px;
  text-align: center;
  box-sizing: border-box;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);

  /* Плавна анімація підстрибування */
  transition:
    transform 0.2s ease,
    box-shadow 0.2s ease;
}

.student-menu__card:hover {
  transform: translateY(-15px);
  box-shadow: 0 25px 40px rgba(0, 0, 0, 0.25);
}

.student-menu__card:active {
  transform: scale(0.95);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}

/* Елемент: Обертка для зображення */
.student-menu__icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 25px;
  height: 130px;
}

/* Елемент: Чисто біле зображення */
.student-menu__image {
  max-width: 120px;
  max-height: 120px;
  object-fit: contain;
  filter: brightness(0) invert(1); /* Перетворює твої PNG на білий колір */
}

/* Елемент: Великий заголовок плитки */
.student-menu__title {
  font-size: 2.6rem;
  font-weight: bold;
  line-height: 1.2;
  margin: 0;
}

/* =========================================
   Блок: student-modal (Модальне вікно контенту)
   ========================================= */
.student-modal__overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(6, 78, 59, 0.7);
  backdrop-filter: blur(8px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.student-modal__content {
  background-color: #ffffff;
  width: 95%;
  max-width: 1400px;
  height: 90vh;
  border-radius: 20px;
  /* ВАЖЛИВО: верхній відступ 80px рятує хрестик від налізання контенту */
  padding: 80px 40px 40px 40px;
  position: relative;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  overflow-y: auto;
  box-sizing: border-box;
}

/* Елемент: Зафіксований та захищений хрестик виходу */
.student-modal__close-btn {
  position: absolute;
  top: 20px;
  right: 20px;
  background: #f1f5f9;
  border: none;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  font-size: 2.5rem;
  color: #334155;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  /* Високий індекс гарантує перебування ПОВЕРХ будь-яких SVG карт */
  z-index: 1100;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition:
    background-color 0.2s ease,
    transform 0.2s ease,
    color 0.2s ease;
}

.student-modal__close-btn:hover {
  background: #ef4444;
  color: #ffffff;
  transform: scale(1.05);
}

.student-modal__close-btn:active {
  transform: scale(0.95);
}

.student-modal__empty-state {
  padding: 4rem;
  text-align: center;
}

.student-modal__empty-title {
  font-size: 2rem;
  font-weight: bold;
}
</style>
