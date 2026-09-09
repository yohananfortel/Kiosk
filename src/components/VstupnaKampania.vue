<template>
  <div class="campaign">
    <div class="campaign__header">
      <h2 class="campaign__title">Вступна кампанія</h2>
    </div>

    <div class="campaign__grid">
      <div
        v-for="item in menuItems"
        :key="item.id"
        class="campaign-card"
        :style="{ backgroundColor: item.color || '#00a53f' }"
        @click="openModal(item)"
      >
        <div class="campaign-card__media">
          <img
            v-if="item.image"
            :src="item.image"
            :alt="item.title"
            class="campaign-card__image"
          />
        </div>
        <h3 class="campaign-card__title">{{ item.title }}</h3>
      </div>
    </div>

    <Transition name="fade">
      <div
        v-if="isModalOpen"
        class="campaign-modal__overlay"
        @click.self="closeModal"
      >
        <div class="campaign-modal__content">
          <button class="campaign-modal__close-btn" @click="closeModal">&times;</button>

          <component :is="activeComponent" v-if="activeComponent" />

          <div v-else class="campaign-modal__empty">
            <h2 class="campaign-modal__empty-title">
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
    color: "#00a53f",
    component: Speciality,
  },
  {
    id: 2,
    title: "Терміни кампанії",
    image: "img/time.png",
    color: "#00a53f",
    component: AdmissionDates,
  },
]);

const openModal = (item) => {
  currentTitle.value = item.title;
  activeComponent.value = item.component || null;
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
  activeComponent.value = null;
};
</script>

<style scoped>
/* ==========================================================================
   Блок: campaign (Вступна кампанія)
   Методологія: БЕМ
   ========================================================================== */

.campaign {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  padding: 20px;
  font-family: system-ui, -apple-system, sans-serif;
}

.campaign__header {
  margin-bottom: 35px;
}

.campaign__title {
  font-size: 2.8rem;
  font-weight: 800;
  color: #166534;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0;
  text-align: center;
}

.campaign__grid {
  display: flex;
  gap: 50px;
  justify-content: center;
  align-items: center;
  width: 100%;
  margin: 0 auto;
}

/* ==========================================================================
   Блок: campaign-card (Велика картка розділу)
   ========================================================================== */

.campaign-card {
  width: 350px;
  height: 320px;
  border-radius: 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  cursor: pointer;
  padding: 30px;
  text-align: center;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.12);
}

.campaign-card:hover {
  transform: translateY(-12px);
  box-shadow: 0 25px 45px rgba(0, 0, 0, 0.22);
}

.campaign-card:active {
  transform: scale(0.96);
}

.campaign-card__media {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
  height: 130px;
}

.campaign-card__image {
  max-width: 120px;
  max-height: 120px;
  object-fit: contain;
  filter: brightness(0) invert(1);
}

.campaign-card__title {
  font-size: 2.4rem;
  font-weight: 800;
  line-height: 1.2;
  margin: 0;
}

/* ==========================================================================
   Блок: campaign-modal (Модальне вікно)
   ========================================================================== */

.campaign-modal__overlay {
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

.campaign-modal__content {
  background-color: #ffffff;
  width: 90%;
  max-width: 1400px;
  height: 88vh;
  border-radius: 24px;
  padding: 35px;
  position: relative;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
  overflow-y: auto;
}

.campaign-modal__close-btn {
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
  color: #475569;
  transition: background-color 0.2s, color 0.2s;
}

.campaign-modal__close-btn:hover {
  background: #e2e8f0;
  color: #0f172a;
}

.campaign-modal__close-btn:active {
  background: #cbd5e1;
  transform: scale(0.92);
}

.campaign-modal__empty {
  padding: 60px 20px;
  text-align: center;
}

.campaign-modal__empty-title {
  font-size: 2rem;
  font-weight: 800;
  color: #64748b;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.25s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
