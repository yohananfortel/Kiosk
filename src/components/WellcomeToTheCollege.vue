<template>
  <div class="dashboard-container">
    <div class="tiles-grid">
      <div
        v-for="item in menuItems"
        :key="item.id"
        class="tile-card"
        :style="{ backgroundColor: item.color }"
        @click="openModal(item)"
      >
        <div class="icon-wrapper">
          <span class="flat-icon">{{ item.icon }}</span>

          <img
            v-if="item.image"
            :src="item.image"
            :alt="item.title"
            class="flat-image"
          />
        </div>
        <h3 class="tile-title">{{ item.title }}</h3>
      </div>
    </div>

    <Transition name="fade">
      <div v-if="isModalOpen" class="modal-overlay" @click.self="closeModal">
        <div class="modal-content">
          <button class="close-btn" @click="closeModal">&times;</button>

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
    link: "/admission",
    component: Abiturientu,
  },
  {
    id: 2,
    title: "Студенту",
    image: "img/student.png",
    color: "#00a53f",
    link: "/student",
    component: Studentu,
  },
  {
    id: 3,
    title: "Контакти",
    image: "img/telephone-call.png",
    color: "#00a53f",
    link: "/contacts",
    component: Contacts,
  },
  {
    id: 4,
    title: "Гуртожиток",
    image: "img/hostel.png",
    color: "#00a53f",
    link: "/dormitory",
    component: Dormitory,
  },
  {
    id: 5,
    title: "Укриття",
    image: "img/location.png",
    color: "#00a53f",
    link: "/shelter",
    component: Shelter,
  },
  {
    id: 6,
    title: "Новини",
    image: "img/news.png",
    color: "#00a53f",
    component: News,
    link: "/news",
  },
]);

const handleNavigate = (link) => {
  console.log(`Перехід до: ${link}`);
  // Тут логіка для vue-router: router.push(link)
};

const openModal = (item) => {
  activeComponent.value = item.component;
  isModalOpen.value = true;
  // Блокуємо скрол основної сторінки
  document.body.style.overflow = "hidden";
};

const closeModal = () => {
  isModalOpen.value = false;
  activeComponent.value = null;
  document.body.style.overflow = "auto";
};
</script>

<style scoped>
/* Сітка для карток на головній сторінці */
.tiles-grid {
  display: flex;
  flex-wrap: wrap; /* Позволяет переносить на новую строку */
  justify-content: center; /* Центрирует все элементы по горизонтали */
  align-items: center;
  gap: 40px; /* Одинаковое расстояние между всеми карточками */
  padding: 20px;
  max-width: 1200px; /* Ограничиваем ширину, чтобы ровно 3 карточки влазили в ряд */
  margin: 0 auto; /* Центрируем сам контейнер на экране */
}

/* Сама картка */
.tile-card {
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

  /* Плавность для анимации */
  transition:
    transform 0.2s ease,
    box-shadow 0.2s ease;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}

/* Анимация подпрыгивания */
.tile-card:hover {
  transform: translateY(-15px);
  box-shadow: 0 25px 40px rgba(0, 0, 0, 0.25);
}

.tile-card:active {
  transform: scale(0.95);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}

/* Стилі для іконок (робимо PNG білими) */
.icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
  height: 120px;
}

.flat-image {
  max-width: 100px;
  max-height: 100px;
  object-fit: contain;
  filter: brightness(0) invert(1); /* Робить кольорові PNG білими */
}

.tile-title {
  font-size: 2.2rem;
  font-weight: bold;
  line-height: 1.2;
}

/* =========================================
   Стилі для модального вікна
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
