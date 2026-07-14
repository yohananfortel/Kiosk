<template>
  <div class="abiturient-menu">
    <div class="abiturient-menu__grid">
      <div
        v-for="item in menuItemsAbit"
        :key="item.id"
        class="abiturient-menu__card"
        :style="{ backgroundColor: item.color || '#00a53f' }"
        @click="openModal(item)"
      >
        <div class="abiturient-menu__icon-wrapper">
          <img
            :src="item.image"
            :alt="item.title"
            class="abiturient-menu__image"
          />
        </div>
        <h3 class="abiturient-menu__title">{{ item.title }}</h3>
      </div>
    </div>

    <Transition name="fade">
      <div v-if="isModalOpen" class="modal-overlay" @click.self="closeModal">
        <div class="modal-content">
          <button class="close-btn" @click="closeModal">&times;</button>

          <component :is="activeComponent" v-if="activeComponent" />

          <div v-else class="modal-empty-state">
            <h2 class="modal-empty-title">
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
import AbiturientMap from "./AbiturientMap.vue";
import Speciality from "./Speciality.vue";

const isModalOpen = ref(false);
const activeComponent = shallowRef(null);
const currentTitle = ref("");

const menuItemsAbit = ref([
  {
    id: 1,
    title: "Карта вступника",
    color: "#00a53f",
    component: AbiturientMap,
    image: "img/route.png",
  },
  {
    id: 2,
    title: "Наші Спеціальності",
    color: "#00a53f",
    component: Speciality,
    image: "img/specialty.png",
  },
  {
    id: 3,
    title: "Державне замовлення",
    color: "#00a53f",
    image: "img/derjavnezamovlena.png",
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
   Блок: abiturient-menu (Меню абітурієнта)
   Методологія: БЕМ
   ========================================= */

.abiturient-menu {
  width: 100%;
  /* Змушуємо контейнер зайняти всю висоту батьківського вікна модалки */
  min-height: 70vh;
  display: flex;
  /* Ідеальне центрування по вертикалі та горизонталі */
  justify-content: center;
  align-items: center;
  padding: 20px;
  box-sizing: border-box;
}

/* Елемент: Контейнер сітки (Симетрія 3-х карток) */
.abiturient-menu__grid {
  display: flex;
  flex-wrap: wrap;
  gap: 40px; /* Фіксований відступ між плитками */
  justify-content: center; /* Рівняє картки строго по центру рядка */
  align-items: center;
  width: 100%;
  max-width: 1150px; /* Обмеження, щоб 3 картки красиво ставали в один ряд */
  margin: 0 auto;
}

/* Елемент: Картка */
.abiturient-menu__card {
  width: 320px;
  height: 320px;
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

  /* Анімація підстрибування */
  transition:
    transform 0.2s ease,
    box-shadow 0.2s ease;
}

.abiturient-menu__card:hover {
  transform: translateY(-15px);
  box-shadow: 0 25px 40px rgba(0, 0, 0, 0.25);
}

.abiturient-menu__card:active {
  transform: scale(0.95);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}

/* Елемент: Обертка іконки */
.abiturient-menu__icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
  height: 120px;
}

/* Елемент: PNG Зображення (Ефект чисто-білого кольору) */
.abiturient-menu__image {
  max-width: 110px;
  max-height: 110px;
  object-fit: contain;
  filter: brightness(0) invert(1);
}

/* Елемент: Текст назви плитки */
.abiturient-menu__title {
  font-size: 2.4rem;
  font-weight: bold;
  line-height: 1.2;
  margin: 0;
}

/* =========================================
   Стилі для модального вікна (Твої рідні)
   ========================================= */
.modal-overlay {
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

.modal-content {
  background-color: #ffffff;
  width: 95%;
  max-width: 1400px;
  height: 90vh;
  border-radius: 20px;
  padding: 40px;
  position: relative;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  overflow-y: auto;
}

.close-btn {
  position: absolute;
  top: 20px;
  right: 20px;
  background: #f1f5f9;
  border: none;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  font-size: 2rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 100;
}

.modal-empty-state {
  padding: 4rem;
  text-align: center;
}

.modal-empty-title {
  font-size: 2rem;
  font-weight: bold;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
