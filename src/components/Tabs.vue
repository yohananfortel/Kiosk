<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  // Очікуємо масив: [{ label: 'Назва', component: Object }]
  items: {
    type: Array,
    required: true
  }
})

const activeIndex = ref(0)

// Обчислюємо поточний компонент для відображення
const activeComponent = computed(() => props.items[activeIndex.value].component)
</script>

<template>
  <div class="tabs-wrapper">
    <!-- Навігація -->
    <div class="tabs-nav">
      <button 
        v-for="(tab, index) in items" 
        :key="index"
        :class="{ active: activeIndex === index }"
        @click="activeIndex = index"
      >
        {{ tab.label }}
      </button>
    </div>

    <!-- Область контенту -->
    <div class="tabs-content">
      <!-- Динамічний рендеринг компонента -->
      <component :is="activeComponent" />
    </div>
  </div>
</template>

<style scoped>
.tabs-nav {
  display: flex;
  gap: 5px;
  background: #f4f4f4;
  padding: 5px;
  border-radius: 8px;
}

button {
  flex: 1;
  padding: 10px;
  border: none;
  background: transparent;
  cursor: pointer;
  border-radius: 6px;
  transition: 0.2s;
}

button.active {
  background: white;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  font-weight: 600;
}

.tabs-content {
  margin-top: 20px;
  padding: 15px;
  border: 1px solid #eee;
  border-radius: 8px;
}
</style>