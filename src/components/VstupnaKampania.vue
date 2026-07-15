<template>
  <div class="vstup-container">
    <div class="vstup-header">
      <h2 class="vstup-title">Вступна кампанія 2026</h2>
    </div>

    <div class="tiles-grid-center">
      <div
        v-for="item in menuItems"
        :key="item.id"
        class="tile-card-large"
        :style="{ backgroundColor: item.color }"
        @click="openModal(item)"
      >
        <div class="icon-wrapper">
          <img
            v-if="item.image"
            :src="item.image"
            :alt="item.title"
            class="flat-image-large"
          />
          <span v-else class="flat-icon-large">{{ item.icon }}</span>
        </div>
        <h3 class="tile-title-large">{{ item.title }}</h3>
      </div>
    </div>

    <Transition name="fade">
      <div v-if="isModalOpen" class="modal-overlay" @click.self="closeModal">
        <div class="modal-content">
          <button class="close-btn" @click="closeModal">&times;</button>

          <component :is="activeComponent" v-if="activeComponent" />

          <div
            v-else
            class="p-10 text-center"
            style="padding: 4rem; text-align: center"
          >
            <h2 class="text-2xl font-bold" style="font-size: 2rem">
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
import Speciality from "./Speciality.vue";
import AdmissionDates from "./AdmissionDates.vue";

const isModalOpen = ref(false);
const activeComponent = shallowRef(null);
const currentTitle = ref("");

const menuItems = ref([
  {
    id: 1,
    title: "Наші спеціальності",
    image: "img/nahispetialnosti.png",
    color: "#00a53f", // Колір з першої сторінки
    component: Speciality,
  },
  {
    id: 2,
    title: "Терміни кампанії",
    image: "img/time.png",
    color: "#00a53f", // Колір з першої сторінки
    component: AdmissionDates,
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
/* Твої рідні налаштування контейнера */
.vstup-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  padding: 2rem;
}

.vstup-header {
  margin-bottom: 40px;
}

.vstup-title {
  padding: auto;
  font-size: 3rem;
  font-weight: 800;
  color: #166534;
  text-transform: uppercase;
}

/* Твоя рідна сітка */
.tiles-grid-center {
  display: flex;
  gap: 60px; /* Делаем отступ между двумя большими картами чуть больше */
  justify-content: center; /* Центрируем по горизонтали */
  align-items: center;
  width: 100%;
  margin: 0 auto; /* Центрируем контейнер */
}

/* Твои классы для карточек (увеличенные) */
.tile-card-large {
  width: 350px; /* Строго фиксированная ширина */
  height: 320px; /* Строго фиксированная высота = идеальный квадрат */
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: white;
  cursor: pointer;
  padding: 30px;
  text-align: center;

  /* Анимация */
  transition:
    transform 0.2s ease,
    box-shadow 0.2s ease;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
  text-align: center;
  padding: 30px;
}

/* Эффект анимации подпрыгивания */
.tile-card-large:hover {
  transform: translateY(-15px);
  box-shadow: 0 25px 40px rgba(0, 0, 0, 0.25);
}

.tile-card-large:active {
  transform: scale(0.95);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}

.icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
  height: 140px;
}

/* Магія для білих PNG */
.flat-image-large {
  max-width: 130px;
  max-height: 130px;
  object-fit: contain;
  filter: brightness(0) invert(1); /* Робить картинку повністю білою */
}

.flat-icon-large {
  font-size: 9rem;
  display: block;
}

.tile-title-large {
  font-size: 3rem;
  font-weight: bold;
  line-height: 1.2;
}

/* Твоя рідна модалка */
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
  width: 90%;
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
