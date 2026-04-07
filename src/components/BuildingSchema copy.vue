<template>
  <div class="map-container">
    <div class="sidebar">
      <h3>Інформація</h3>
      <div v-if="selectedRoom" class="room-info">
        <p><strong>Аудиторія:</strong> {{ selectedRoom.id }}</p>
        <p><strong>Тип:</strong> {{ selectedRoom.type }}</p>
        <p><strong>Поверх:</strong> {{ selectedRoom.floor }}</p>
      </div>
      <div v-else class="room-info-empty">
        Оберіть аудиторію на схемі
      </div>
    </div>

    <div class="svg-wrapper">
      <svg viewBox="0 0 800 800" class="interactive-map">
        <!-- Глобальний зсув, щоб відцентрувати будівлю -->
        <g transform="translate(400, 150)">
          
          <!-- 
            Рендеримо поверхи. 
            ВАЖЛИВО: рендеримо від 1 до 3 поверху (reverse), 
            щоб верхні поверхи візуально перекривали нижні.
          -->
          <g v-for="floor in floors" :key="floor.level" 
             :transform="`translate(0, ${floor.offsetY})`" 
             class="floor-group">

            <!-- Назва поверху -->
            <text x="-250" y="50" class="floor-title">Поверх {{ floor.level }}</text>

            <!-- 
              МАГІЯ ІЗОМЕТРІЇ:
              scale(1, 0.5) - стискає по вертикалі
              rotate(-45) - розгортає ромбом
            -->
            <g transform="scale(1, 0.6) rotate(-35)">
              
              <!-- Основа поверху (підлога) -->
              <rect x="0" y="0" :width="floor.width" :height="floor.height" class="floor-slab" />

              <!-- Аудиторії (малюються як звичайні 2D прямокутники) -->
              <g v-for="room in floor.rooms" :key="room.id" 
                 class="room" 
                 :class="{ 'is-selected': selectedRoom?.id === room.id }"
                 @click="selectRoom(room, floor.level)">
                
                <rect 
                  :x="room.x" 
                  :y="room.y" 
                  :width="room.w" 
                  :height="room.h" 
                  :fill="getRoomColor(room.type)"
                  class="room-shape" 
                />

                <!-- 
                  Текст: обертаємо на 45 градусів навколо свого центру, 
                  щоб компенсувати поворот батьківської групи і зробити його горизонтальним 
                -->
                <text 
                  :x="room.x + room.w / 2" 
                  :y="room.y + room.h / 2"
                  text-anchor="middle" 
                  dominant-baseline="central"
                  :transform="`rotate(45, ${room.x + room.w / 2}, ${room.y + room.h / 2})`"
                  class="room-label">
                  {{ room.id }}
                </text>
              </g>
            </g>
          </g>
        </g>
      </svg>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Стан вибраної кімнати
const selectedRoom = ref(null)

// Вибір кімнати та додавання до неї номера поверху
const selectRoom = (room, floorLevel) => {
  selectedRoom.value = { ...room, floor: floorLevel }
}

// Кольори для різних типів аудиторій
const getRoomColor = (type) => {
  const colors = {
    'Лекційна': '#90caf9',
    'Практична': '#a5d6a7',
    'Лабораторія': '#ffab91',
    'Коридор': '#e0e0e0'
  }
  return colors[type] || '#fff'
}

// Дані будівлі. Зверніть увагу: ми малюємо в звичайних 2D координатах (X, Y)!
const buildingData = [
  {
    level: 3,
    offsetY: 0, // Найвищий поверх
    width: 300, // Розмір всієї плити поверху
    height: 200,
    rooms: [
      { id: '301', type: 'Лекційна', x: 10, y: 10, w: 130, h: 80 },
      { id: '302', type: 'Практична', x: 150, y: 10, w: 140, h: 80 },
      { id: '303', type: 'Лабораторія', x: 10, y: 110, w: 280, h: 80 }
    ]
  },
  {
    level: 2,
    offsetY: 180, // Зсув вниз екрану
    width: 300,
    height: 200,
    rooms: [
      { id: '201', type: 'Практична', x: 10, y: 10, w: 90, h: 80 },
      { id: '202', type: 'Практична', x: 110, y: 10, w: 80, h: 80 },
      { id: '203', type: 'Практична', x: 200, y: 10, w: 90, h: 80 },
      { id: '204', type: 'Лекційна', x: 10, y: 110, w: 280, h: 80 }
    ]
  },
  {
    level: 1,
    offsetY: 360, // Найнижчий поверх
    width: 300,
    height: 200,
    rooms: [
      { id: '101', type: 'Лекційна', x: 10, y: 10, w: 130, h: 180 },
      { id: '102', type: 'Лабораторія', x: 150, y: 10, w: 140, h: 80 },
      { id: '103', type: 'Практична', x: 150, y: 100, w: 140, h: 90 }
    ]
  }
]

// Рендеримо знизу (1 поверх) догори (3 поверх), щоб уникнути проблем з перекриттям SVG
const floors = computed(() => {
  return [...buildingData].reverse()
})
</script>

<style scoped>
.map-container {
  display: flex;
  width: 100%;
  height: 800px;
  background-color: #f8f9fa;
  font-family: Arial, sans-serif;
}

.sidebar {
  width: 250px;
  padding: 20px;
  background: white;
  border-right: 1px solid #ddd;
  box-shadow: 2px 0 5px rgba(0,0,0,0.05);
  z-index: 10;
}

.room-info p {
  margin: 10px 0;
  font-size: 16px;
  color: #333;
}

.room-info-empty {
  color: #888;
  font-style: italic;
  margin-top: 20px;
}

.svg-wrapper {
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}

.interactive-map {
  width: 100%;
  height: 100%;
}

.floor-title {
  font-size: 24px;
  font-weight: bold;
  fill: #666;
  pointer-events: none;
}

.floor-slab {
  fill: #e9ecef;
  stroke: #adb5bd;
  stroke-width: 4;
  /* Додаємо тінь для ефекту товщини плити */
  filter: drop-shadow(4px 4px 0px #ced4da);
}

.room {
  cursor: pointer;
  transition: transform 0.2s ease;
}

.room-shape {
  stroke: white;
  stroke-width: 3;
  transition: all 0.3s ease;
}

/* Ефекти наведення */
.room:hover .room-shape {
  fill: #ffca28 !important; /* Жовтий при наведенні */
  transform: translate(-2px, -2px); /* Легкий ефект підняття */
}

/* Стан виділення */
.room.is-selected .room-shape {
  fill: #ff9800 !important;
  stroke: #e65100;
  stroke-width: 4;
}

.room-label {
  font-size: 18px;
  font-weight: bold;
  fill: #333;
  pointer-events: none; /* Щоб клік проходив крізь текст на прямокутник */
  user-select: none;
}
</style>