<template>
  <div class="map-container">
    <div class="sidebar">
      <h3>Інформація</h3>
      <p v-if="selectedRoom">Вибрано аудиторію: <strong>{{ selectedRoom }}</strong></p>
      <p v-else>Клікніть на аудиторію</p>
    </div>

    <div class="svg-wrapper">
      <!-- 
        Один великий SVG контейнер для всієї будівлі.
        viewBox налаштуйте під ваші потреби (ширина/висота загальної сцени) 
      -->
      <svg viewBox="0 0 1000 1000" class="interactive-map">
        
        <!-- Загальний контейнер будівлі для центрування -->
        <g transform="translate(500, 150)">
          
          <!-- ========================================== -->
          <!-- ПОВЕРХ 3 (малюється першим, щоб бути позаду/знизу у DOM, але візуально зверху) -->
          <!-- ========================================== -->
          <g transform="translate(0, 0)" class="floor-group">
            <text x="-350" y="50" class="floor-title">Третій поверх</text>
            
            <!-- Магія ізометрії + Делегування кліку -->
            <g transform="scale(1.1, 0.3) rotate(-25)" @click="handleRoomClick" class="floor-plan">
              
              <!-- Основа поверху (підлога) -->
              <path 
       d="m 21.143301,21.549903 v 91.078837 l 168.333209,-0.4066 -0.8132,-91.485441 -46.35263,-0.406601 V 66.276119 H 69.935536 l 0.813202,-45.946021 z"
       class="floor-base" />

       
              <!-- 
                СЮДИ ВСТАВЛЯЄТЕ ВАШ SVG З FIGMA/ILLUSTRATOR 
                Головне, щоб фігури мали id, які починаються з "room-"
              -->
              
              
            </g>
          </g>

          <!-- ========================================== -->
          <!-- ПОВЕРХ 2 (зміщений вниз на 250px) -->
          <!-- ========================================== -->
          <g transform="translate(0, 250)" class="floor-group">
            <text x="-350" y="50" class="floor-title">Другий поверх</text>
            
            <g transform="scale(1.1, 0.3) rotate(-25)" @click="handleRoomClick" class="floor-plan">
              <path
       d="m 21.143301,21.549903 v 91.078837 l 168.333209,-0.4066 -0.8132,-91.485441 -46.35263,-0.406601 V 66.276119 H 69.935536 l 0.813202,-45.946021 z"
       class="floor-base" />
              
              <!-- ВСТАВЛЯЄТЕ SVG ДЛЯ 2 ПОВЕРХУ -->
              
            </g>
          </g>

          <g transform="translate(0, 500)" class="floor-group">
            <text x="-350" y="50" class="floor-title">Перший поверх</text>
            
            <g transform="scale(1, 0.5) rotate(-25)" @click="handleRoomClick" class="floor-plan">
              <path 
       d="m 21.143301,21.549903 v 91.078837 l 168.333209,-0.4066 -0.8132,-91.485441 -46.35263,-0.406601 V 66.276119 H 69.935536 l 0.813202,-45.946021 z"
       class="floor-base" />
              
              <!-- ВСТАВЛЯЄТЕ SVG ДЛЯ 2 ПОВЕРХУ -->
              
            </g>
          </g>

        </g>
      </svg>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const selectedRoom = ref(null)

// Обробник кліку для всіх поверхів
const handleRoomClick = (event) => {
  // Отримуємо елемент, по якому клікнули
  const target = event.target
  
  // Перевіряємо, чи має елемент id і чи це саме аудиторія (містить "room-")
  if (target && target.id && target.id.startsWith('room-')) {
    // Відрізаємо "room-", залишаємо тільки номер (наприклад, "301")
    selectedRoom.value = target.id.replace('room-', '')
    
    // Візуальне виділення активної кімнати через DOM (можна і через прив'язку класів Vue, 
    // але для сирого SVG з редактора цей спосіб працює найкраще)
    document.querySelectorAll('.is-active').forEach(el => el.classList.remove('is-active'))
    target.classList.add('is-active')
  }
}
</script>

<style scoped>
.map-container {
  display: flex;
  height: 800px;
  background-color: #f4f6f8;
  font-family: sans-serif;
}

.sidebar {
  width: 250px;
  padding: 20px;
  background: white;
  border-right: 1px solid #ddd;
}

.svg-wrapper {
  flex: 1;
  overflow: hidden;
}

.interactive-map {
  width: 100%;
  height: 100%;
}

.floor-title {
  font-size: 24px;
  font-weight: bold;
  fill: #555;
}

/* Стиль основи поверху (підлога) */
.floor-base {
  fill: #e2e8f0;
  stroke: #cbd5e1;
  stroke-width: 2;
  filter: drop-shadow(5px 5px 0px #94a3b8); /* Ефект товщини перекриття */
}

/* Базові стилі для фігур, які ви імпортуєте з графічного редактора */
.room-shape {
  fill: #bae6fd;
  stroke: #ffffff;
  stroke-width: 3;
  cursor: pointer;
  transition: all 0.3s ease;
}

/* Ефект наведення (працює автоматично на всі SVG фігури з класом) */
.room-shape:hover {
  fill: #7dd3fc;
  /* Легкий візуальний підйом */
  transform: translate(-3px, -3px);
  filter: drop-shadow(3px 3px 2px rgba(0,0,0,0.2));
}

/* Клас активної (вибраної) кімнати */
.room-shape.is-active {
  fill: #f59e0b;
  stroke: #b45309;
  stroke-width: 4;
}
</style>