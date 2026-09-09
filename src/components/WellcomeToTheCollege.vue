<template>
  <div class="dashboard">
    <div class="dashboard__grid">
      <div
        v-for="item in menuItems"
        :key="item.id"
        class="dashboard-tile"
        :style="{ backgroundColor: item.color || '#00a53f' }"
        @click="openModal(item)"
      >
        <div class="dashboard-tile__media">
          <img
            v-if="item.image"
            :src="item.image"
            :alt="item.title"
            class="dashboard-tile__image"
          />
        </div>
        <h3 class="dashboard-tile__title">{{ item.title }}</h3>
      </div>
    </div>

    <!-- Модальне вікно підрозділу -->
    <Transition name="fade">
      <div
        v-if="isModalOpen"
        class="dashboard-modal__overlay"
        @click.self="closeModal"
      >
        <div class="dashboard-modal__content">
          <button class="dashboard-modal__close-btn" @click="closeModal">&times;</button>
          <component :is="activeComponent" />
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, shallowRef } from "vue";
import Abiturientu from "./Abiturientu.vue";
import Studentu from "./Studentu.vue";
import Shelter from "./Shelter.vue";
import Contacts from "./Contacts.vue";
import Dormitory from "./Dormitory.vue";
import News from "./News.vue";

const isModalOpen = ref(false);
const activeComponent = shallowRef(null);

const menuItems = ref([
  {
    id: 1,
    title: "Абітурієнту",
    image: "img/abiturient.png",
    color: "#00a53f",
    component: Abiturientu,
  },
  {
    id: 2,
    title: "Студенту",
    image: "img/student.png",
    color: "#00a53f",
    component: Studentu,
  },
  {
    id: 3,
    title: "Контакти",
    image: "img/telephone-call.png",
    color: "#00a53f",
    component: Contacts,
  },
  {
    id: 4,
    title: "Гуртожиток",
    image: "img/hostel.png",
    color: "#00a53f",
    component: Dormitory,
  },
  {
    id: 5,
    title: "Укриття",
    image: "img/location.png",
    color: "#00a53f",
    component: Shelter,
  },
  {
    id: 6,
    title: "Новини",
    image: "img/news.png",
    color: "#00a53f",
    component: News,
  },
]);

const openModal = (item) => {
  activeComponent.value = item.component;
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
  activeComponent.value = null;
};

// Експортуємо closeModal, щоб батьківський App.vue міг закривати модалки при таймауті
defineExpose({
  closeModal,
  isModalOpen,
});
</script>

<style scoped>
/* ==========================================================================
   Блок: dashboard (Головне навігаційне меню кіоску)
   Методологія: БЕМ
   ========================================================================== */

.dashboard {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px;
}

.dashboard__grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 35px;
  padding: 10px;
  max-width: 1200px;
  margin: 0 auto;
}

/* ==========================================================================
   Блок: dashboard-tile (Плитка головного меню)
   ========================================================================== */

.dashboard-tile {
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

.dashboard-tile:hover {
  transform: translateY(-12px);
  box-shadow: 0 25px 45px rgba(0, 0, 0, 0.22);
}

.dashboard-tile:active {
  transform: scale(0.96);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
}

.dashboard-tile__media {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
  height: 110px;
}

.dashboard-tile__image {
  max-width: 100px;
  max-height: 100px;
  object-fit: contain;
  filter: brightness(0) invert(1);
}

.dashboard-tile__title {
  font-size: 2.2rem;
  font-weight: 800;
  line-height: 1.2;
  margin: 0;
}

/* ==========================================================================
   Блок: dashboard-modal (Модальне вікно підрозділу)
   ========================================================================== */

.dashboard-modal__overlay {
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

.dashboard-modal__content {
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

.dashboard-modal__close-btn {
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
  z-index: 10;
}

.dashboard-modal__close-btn:hover {
  background: #e2e8f0;
  color: #0f172a;
}

.dashboard-modal__close-btn:active {
  background: #cbd5e1;
  transform: scale(0.92);
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
