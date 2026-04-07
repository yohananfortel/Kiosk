<template>
  <div class="building-container">
    <svg viewBox="0 0 800 600" preserveAspectRatio="xMidYMid meet" class="isometric-svg">
      <!-- Визначення стилів та градієнтів -->
      <defs>
        <linearGradient id="floorGradient" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" style="stop-color:#f8f9fa;stop-opacity:1" />
          <stop offset="100%" style="stop-color:#e9ecef;stop-opacity:1" />
        </linearGradient>
      </defs>

      <!-- Поверх 3 -->
      <g class="floor-group" transform="translate(400, 150)">
        <FloorLayer 
          :floor-number="3" 
          :rooms="rooms.floor3" 
          color="#a5d6a7" 
          @room-click="handleRoomClick"
        />
      </g>

      <!-- Поверх 2 -->
      <g class="floor-group" transform="translate(400, 300)">
        <FloorLayer 
          :floor-number="2" 
          :rooms="rooms.floor2" 
          color="#90caf9" 
          @room-click="handleRoomClick"
        />
      </g>

      <!-- Поверх 1 -->
      <g class="floor-group" transform="translate(400, 450)">
        <FloorLayer 
          :floor-number="1" 
          :rooms="rooms.floor1" 
          color="#ffab91" 
          @room-click="handleRoomClick"
        />
      </g>
    </svg>

    <!-- Інфо-панель -->
    <div v-if="selectedRoom" class="info-overlay">
      Аудиторія: <strong>{{ selectedRoom }}</strong>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue';
import FloorLayer from './FloorLayer.vue';

const selectedRoom = ref<string | null>(null);

const rooms = reactive({
  floor3: ['301', '302', '303', '304'],
  floor2: ['201', '202', '203', '204'],
  floor1: ['1', '2', 'Конференц зала', 'Бібліотека']
});

const handleRoomClick = (roomNumber: string) => {
  selectedRoom.value = roomNumber;
};
</script>

<style scoped>
.building-container {
  width: 100%;
  height: 600px;
  background-color: #f0f2f5;
  position: relative;
  display: flex;
  justify-content: center;
}

.isometric-svg {
  width: 100%;
  height: 100%;
}

.info-overlay {
  position: absolute;
  bottom: 20px;
  right: 20px;
  background: white;
  padding: 10px 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  font-family: sans-serif;
}
</style>