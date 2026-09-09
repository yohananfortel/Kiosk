<template>
  <div class="student-menu">
    <div class="student-menu__grid">
      <div
        v-for="item in menuItemsStudent"
        :key="item.id"
        class="student-card"
        :style="{ backgroundColor: item.color || '#00a53f' }"
        @click="openModal(item)"
      >
        <div class="student-card__media">
          <img
            v-if="item.image"
            :src="item.image"
            :alt="item.title"
            class="student-card__image"
          />
        </div>
        <h3 class="student-card__title">{{ item.title }}</h3>
      </div>
    </div>

    <!-- Модальне вікно для карти аудиторій або розкладу -->
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

          <div v-else class="student-modal__empty">
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
import Schedule from "./Schedule.vue"; // Оновлений імпорт з правильним написанням

const isModalOpen = ref(false);
const activeComponent = shallowRef(null);
const currentTitle = ref("");

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
   Блок: student-menu (Меню для студентів)
   Методологія: БЕМ
   ========================================================================== */

.student-menu {
  width: 100%;
  min-height: 65vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  font-family: system-ui, -apple-system, sans-serif;
}

.student-menu__grid {
  display: flex;
  flex-wrap: wrap;
  gap: 40px;
  justify-content: center;
  align-items: center;
  max-width: 1000px;
  margin: 0 auto;
}

/* ==========================================================================
   Блок: student-card (Картка меню студента)
   ========================================================================== */

.student-card {
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

.student-card:hover {
  transform: translateY(-12px);
  box-shadow: 0 25px 45px rgba(0, 0, 0, 0.22);
}

.student-card:active {
  transform: scale(0.96);
}

.student-card__media {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
  height: 110px;
}

.student-card__image {
  max-width: 100px;
  max-height: 100px;
  object-fit: contain;
  filter: brightness(0) invert(1);
}

.student-card__title {
  font-size: 2.2rem;
  font-weight: 800;
  line-height: 1.2;
  margin: 0;
}

/* ==========================================================================
   Блок: student-modal (Модальне вікно)
   ========================================================================== */

.student-modal__overlay {
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

.student-modal__content {
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

.student-modal__close-btn {
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

.student-modal__close-btn:hover {
  background: #e2e8f0;
  color: #0f172a;
}

.student-modal__close-btn:active {
  background: #cbd5e1;
  transform: scale(0.92);
}

.student-modal__empty {
  padding: 60px 20px;
  text-align: center;
}

.student-modal__empty-title {
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
