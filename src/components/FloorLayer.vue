<template>
  <g class="floor-layer">
    <!-- Основна плита поверху -->
    <path 
      d="M -200 0 L 0 -100 L 200 0 L 0 100 Z" 
      fill="url(#floorGradient)" 
      stroke="#ccc" 
      stroke-width="1"
    />
    
    <!-- Спрощене розбиття на аудиторії -->
    <g v-for="(room, index) in rooms" :key="room" 
       class="room-cell" 
       @click="$emit('room-click', room)">
      
      <!-- Розрахунок координат для кожної кімнати -->
      <path 
        :d="getRoomPath(index)" 
        :fill="color" 
        class="room-polygon"
      />
      
      <!-- Номер аудиторії -->
      <text 
        :x="getTextCoords(index).x" 
        :y="getTextCoords(index).y" 
        text-anchor="middle" 
        class="room-label">
        {{ room }}
      </text>
    </g>

    <!-- Позначка поверху -->
    <text x="-220" y="0" class="floor-label">Поверх {{ floorNumber }}</text>
  </g>
</template>

<script setup lang="ts">
const props = defineProps<{
  floorNumber: number;
  rooms: string[];
  color: string;
}>();

defineEmits(['room-click']);

// Функція для малювання ромбоподібних частин кімнат
const getRoomPath = (index: number) => {
  const offset = (index - 1.5) * 80;
  return `M ${offset - 35} 0 L ${offset} -20 L ${offset + 35} 0 L ${offset} 20 Z`;
};

const getTextCoords = (index: number) => {
  return { x: (index - 1.5) * 80, y: 5 };
};
</script>

<style scoped>
.room-polygon {
  cursor: pointer;
  transition: all 0.3s ease;
  stroke: rgba(255,255,255,0.5);
}

.room-polygon:hover {
  filter: brightness(0.9);
  transform: translateY(-5px);
}

.room-label {
  font-family: Arial, sans-serif;
  font-size: 12px;
  font-weight: bold;
  pointer-events: none;
  fill: #333;
}

.floor-label {
  font-family: sans-serif;
  font-weight: bold;
  fill: #666;
}
</style>