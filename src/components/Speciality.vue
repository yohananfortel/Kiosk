<script setup>
import { ref, onMounted } from 'vue'

const selectedSpecialty = ref(null)

const specialties = ref([])
const loading = ref(true)
const error = ref(null)

const fetchSpecialties = async () => {
  try {
    // Вкажіть правильний базовий URL вашого WordPress сайту
    const response = await fetch('//ocsnau.net/wp-json/spa/v1/specialties')
    
    if (!response.ok) {
      throw new Error('Помилка при завантаженні даних')
    }
    
    specialties.value = await response.json()

    console.log('Завантажені спеціальності:', specialties.value)
  } catch (err) {
    error.value = err.message
    console.error('Помилка при завантаженні спеціальностей:', err)
  } finally {
    loading.value = false
  }
}

const openModal = (specialty) => {
  selectedSpecialty.value = specialty
}

const closeModal = () => {
  selectedSpecialty.value = null
}

onMounted(() => {
  fetchSpecialties()
})
</script>

<template>

      <h1>Спеціальності нашого закладу</h1>
        <p>Оберіть спеціальність для отримання детальної інформації</p> 
 <main class="grid-container">
      <div 
        v-for="item in specialties" 
        
        :key="item.id" 
        class="tile"
        @click="openModal(item)"
      >
        <img v-if="item.thumbnail" :src="item.thumbnail" alt="Specialty image" />
      
        <h3 class="tile-title-small">{{ item.title }}</h3>
      </div>
    </main>

    <Teleport to="body">
      <Transition name="modal">
        <div v-if="selectedSpecialty" class="modal-overlay" @click.self="closeModal">
          <div class="modal-content">
            <button class="close-btn" @click="closeModal">✕ Закрити</button>
            
            <div class="modal-header">
             
              <h2>{{ selectedSpecialty.name }}</h2>
            </div>
            
            <div class="modal-body">
              <p><span class="bold">Термін навчання:</span> {{ selectedSpecialty.l }}</p>
              
              <p><span class="bold">Опис:</span> {{ selectedSpecialty.description }}</p>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  
</template>

<style scoped>

/* Сітка плиток */
.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 1rem;
  flex: 1;
  align-content: start;
}
.tile-title-small {
  font-size: 2em;
}

</style>