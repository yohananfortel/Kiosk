<template>
  <div class="tiles-grid">
    <div 
      v-for="item in menuItemsAbit" 
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

    <Transition name="fade">
      <div v-if="isModalOpen" class="modal-overlay" @click.self="closeModal">
        <div class="modal-content">
          <button class="close-btn" @click="closeModal">&times;</button>
          
          <component :is="activeComponent" v-if="activeComponent" />
          
          <div v-else class="p-10 text-center">
            <h2 class="text-2xl font-bold">Розділ "{{ currentTitle }}" знаходиться у розробці</h2>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, shallowRef } from 'vue';

import BuildSchema from './BuildSchema.vue'

// Стан модального вікна
const isModalOpen = ref(false);
const activeComponent = shallowRef(null);
const currentTitle = ref('');

const menuItemsAbit = ref([
  { id: 1, title: "Карта аудиторій", color: '#00a53f', component: BuildSchema, image: 'img/route.png' },
  { id: 2, title: "Розклад занять"}
]);

const openModal = (item) => {
  currentTitle.value = item.title;
  activeComponent.value = item.component || null;
  isModalOpen.value = true;
  document.body.style.overflow = 'hidden';
};

const closeModal = () => {
  isModalOpen.value = false;
  activeComponent.value = null;
  document.body.style.overflow = 'auto';
};
</script>

<style scoped>
/* Сітка плиток */
.tiles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  padding: 20px;
}

.tile-card {
  aspect-ratio: 1 / 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 20px;
  color: white;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  text-align: center;
  padding: 20px;
}

.tile-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}


.flat-icon {
  font-size: 4rem;
}


</style>