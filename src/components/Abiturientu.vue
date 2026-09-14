<template>
  <div class="applicant-menu">
    <div class="applicant-menu__grid">
      <div
        v-for="item in menuItemsAbit"
        :key="item.id"
        class="applicant-card"
        :style="{ backgroundColor: item.color || '#00a53f' }"
        @click="openModal(item)"
      >
        <div class="applicant-card__media">
          <img
            :src="item.image"
            :alt="item.title"
            class="applicant-card__image"
          />
        </div>
        <h3 class="applicant-card__title">{{ item.title }}</h3>
      </div>
    </div>

    <!-- Модальне вікно для карти вступника або спеціальностей -->
    <Transition name="fade">
      <div
        v-if="isModalOpen"
        class="applicant-modal__overlay"
        @click.self="closeModal"
      >
        <div class="applicant-modal__content">
          <button class="applicant-modal__close-btn" @click="closeModal">&times;</button>

          <component :is="activeComponent" v-if="activeComponent" />

          <div v-else class="applicant-modal__empty">
            <h2 class="applicant-modal__empty-title">
              Розділ "{{ currentTitle }}" знаходиться у розробці
            </h2>
            <p class="applicant-modal__empty-desc">
              Актуальні обсяги держзамовлення оновлюються приймальною комісією.
            </p>
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
import AdmissionDates from "./AdmissionDates.vue";

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
    title: "Терміни кампанії",
    color: "#00a53f",
    component: AdmissionDates,
    image: "img/derjavnezamovlena.png",
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

defineExpose({
  closeModal,
  isModalOpen,
});
</script>

<style scoped>
/* ==========================================================================
   Блок: applicant-menu (Меню для абітурієнтів)
   Методологія: БЕМ
   ========================================================================== */

.applicant-menu {
  width: 100%;
  min-height: 65vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  font-family: system-ui, -apple-system, sans-serif;
}

.applicant-menu__grid {
  display: flex;
  flex-wrap: wrap;
  gap: 35px;
  justify-content: center;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
}

/* ==========================================================================
   Блок: applicant-card (Картка меню абітурієнта)
   ========================================================================== */

.applicant-card {
  width: 350px;
  height: 310px;
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

.applicant-card:hover {
  transform: translateY(-12px);
  box-shadow: 0 25px 45px rgba(0, 0, 0, 0.22);
}

.applicant-card:active {
  transform: scale(0.96);
}

.applicant-card__media {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
  height: 110px;
}

.applicant-card__image {
  max-width: 100px;
  max-height: 100px;
  object-fit: contain;
  filter: brightness(0) invert(1);
}

.applicant-card__title {
  font-size: 2.2rem;
  font-weight: 800;
  line-height: 1.2;
  margin: 0;
}

/* ==========================================================================
   Блок: applicant-modal (Модальне вікно)
   ========================================================================== */

.applicant-modal__overlay {
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
  z-index: 1050;
}

.applicant-modal__content {
  background-color: #ffffff;
  width: 92%;
  max-width: 1400px;
  height: 88vh;
  border-radius: 24px;
  padding: 35px;
  position: relative;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
  overflow-y: auto;
}

.applicant-modal__close-btn {
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
  z-index: 10;
  transition: background-color 0.2s, color 0.2s;
}

.applicant-modal__close-btn:hover {
  background: #e2e8f0;
  color: #0f172a;
}

.applicant-modal__close-btn:active {
  background: #cbd5e1;
  transform: scale(0.92);
}

.applicant-modal__empty {
  padding: 60px 20px;
  text-align: center;
}

.applicant-modal__empty-title {
  font-size: 2.2rem;
  font-weight: 800;
  color: #166534;
  margin-bottom: 12px;
}

.applicant-modal__empty-desc {
  font-size: 1.3rem;
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
