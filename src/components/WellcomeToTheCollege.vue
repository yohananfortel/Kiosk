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
import { ref, shallowRef } from 'vue';
import Abiturientu from './Abiturientu.vue';
import Studentu from './Studentu.vue'
import Shelter from './Shelter.vue';
import Contacts from './Contacts.vue';

const isModalOpen = ref(false);
const activeComponent = shallowRef(null);

const menuItems = ref([
  { id: 1, title: 'Абітурієнту', image: 'img/abiturient.png', color: '#00a53f', link: '/admission', component: Abiturientu },
  { id: 2, title: 'Студенту',  image: 'img/student.png', color: '#00a53f', link: '/student', component: Studentu},
  { id: 3, title: 'Контакти', image: 'img/telephone-call.png', color: '#00a53f', link: '/contacts', component: Contacts },
  { id: 4, title: 'Гуртожиток', image: 'img/hostel.png', color: '#00a53f', link: '/dormitory' },
  { id: 5, title: 'Укриття', image: 'img/location.png', color: '#00a53f', link: '/shelter', component: Shelter },
]);

const handleNavigate = (link) => {
  console.log(`Перехід до: ${link}`);
  // Тут логіка для vue-router: router.push(link)
};

const openModal = (item) => {
  activeComponent.value = item.component;
  isModalOpen.value = true;
  // Блокуємо скрол основної сторінки
  document.body.style.overflow = 'hidden';
};

const closeModal = () => {
  isModalOpen.value = false;
  activeComponent.value = null;
  document.body.style.overflow = 'auto';
};

</script>

<style scoped>


</style>