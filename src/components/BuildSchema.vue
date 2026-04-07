<template>
  <div class="map-container">
    <div class="sidebar">
      <h3>Інформація</h3>
      <p v-if="selectedRoom">Вибрано аудиторію: <strong>{{ selectedRoom }}</strong></p>
      <p v-else>Клікніть на аудиторію</p>

      <hr />

     
    </div>

    <div class="svg-wrapper">
      <svg viewBox="0 0 500 500" class="interactive-map">
        
        <!-- Загальний контейнер будівлі для центрування -->
        <g transform="translate(100, 50)">
          
          <!-- ========================================== -->
          <!-- ПОВЕРХ 3 -->
          <!-- ========================================== -->
          <g transform="translate(0, 0)" class="floor-group">
            <text x="-150" y="50" class="floor-title">ІІІ поверх</text>
            
            <g :transform="isometricTransform" @click="handleRoomClick" class="floor-plan">
              <path 
                d="m 21.143301,21.549903 v 91.078837 l 168.333209,-0.4066 -0.8132,-91.485441 -46.35263,-0.406601 V 66.276119 H 69.935536 l 0.813202,-45.946021 z"
                class="floor-base" 
              />
              <!-- СЮДИ ВСТАВЛЯЄТЕ ВАШ SVG З FIGMA/ILLUSTRATOR -->

              <rect
       style="fill:#ffcc00;stroke-width:0.264583"
       id="room-rect2"
       width="16.817284"
       height="24.024693"
       x="23.123766"
       y="55.557098" />
    <rect
       style="fill:#ffcc00;stroke-width:0.264583"
       id="room-rect3"
       width="42.643826"
       height="12.913271"
       x="21.922531"
       y="98.801544"
       ry="0" />
    <rect
       style="fill:#ffcc00;stroke-width:0.264583"
       id="room-rect4"
       width="18.619135"
       height="29.129936"
       x="169.07378"
       y="21.321913" />
    <rect
       style="fill:#ffcc00;stroke-width:0.264583"
       id="room-rect5"
       width="16.516975"
       height="22.523148"
       x="171.47624"
       y="53.154629" />
    <rect
       style="fill:#ffcc00;stroke-width:0.264583"
       id="room-rect1"
       width="17.4179"
       height="31.532406"
       x="23.123766"
       y="22.222839" />
    <rect
       style="fill:#ffcc00;stroke-width:0.264583"
       id="room-rect7"
       width="66.067894"
       height="32.433334"
       x="71.473457"
       y="78.380554"
       ry="0" />
    <rect
       style="fill:#ffcc00;stroke-width:0.264583"
       id="room-rect6"
       width="45.346607"
       height="14.715123"
       x="143.84784"
       y="96.999687" /> 

           <text
       xml:space="preserve"
       style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#24221c;stroke-width:0.264583"
       x="-53.124767"
       y="32.546249"
       id="room-text11"
       transform="rotate(-90.715607)"><tspan
         sodipodi:role="line"
         id="room-tspan11"
         style="stroke-width:0.264583"
         x="-53.124767"
         y="32.546249">Аудиторія №11</tspan></text>
    <rect
       style="fill:#ffcc00;stroke-width:0.264583"
       id="room-rect6"
       width="45.346607"
       height="14.715123"
       x="143.84784"
       y="96.999687" />
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#24221c;stroke-width:0.264583"
       x="-85.930687"
       y="32.136612"
       id="room-text16"
       transform="rotate(-90.715607)"><tspan
         sodipodi:role="line"
         id="room-tspan13"
         style="stroke-width:0.264583"
         x="-85.930687"
         y="32.136612">Аудиторія №11</tspan></text>
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#24221c;stroke-width:0.264583"
       x="27.385025"
       y="106.33826"
       id="room-text17"><tspan
         sodipodi:role="line"
         id="room-tspan16"
         style="stroke-width:0.264583"
         x="27.385025"
         y="106.33826">Аудиторія №12</tspan></text>
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#24221c;stroke-width:0.264583"
       x="-55.885952"
       y="181.47647"
       id="room-text18"
       transform="rotate(-90.715607)"><tspan
         sodipodi:role="line"
         id="room-tspan17"
         style="stroke-width:0.264583"
         x="-55.885952"
         y="181.47647">Аудиторія №11</tspan></text>
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#24221c;stroke-width:0.264583"
       x="-87.104362"
       y="180.18555"
       id="room-text19"
       transform="rotate(-90.715607)"><tspan
         sodipodi:role="line"
         id="room-tspan18"
         style="stroke-width:0.264583"
         x="-87.104362"
         y="180.18555">Аудиторія №11</tspan></text>
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#24221c;stroke-width:0.264583"
       x="151.11218"
       y="105.73764"
       id="room-text20"><tspan
         sodipodi:role="line"
         id="room-tspan19"
         style="stroke-width:0.264583"
         x="151.11218"
         y="105.73764">Аудиторія №13</tspan></text>
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#24221c;stroke-width:0.264583"
       x="90.837196"
       y="94.02562"
       id="room-text21"><tspan
         sodipodi:role="line"
         id="room-tspan20"
         style="stroke-width:0.264583"
         x="90.837196"
         y="94.02562">Актова зала</tspan></text>

            </g>
          </g>

          <!-- ========================================== -->
          <!-- ПОВЕРХ 2 -->
          <!-- ========================================== -->
          <!-- Зміщення розраховується динамічно на основі floorGap -->
          <g :transform="`translate(0, ${isoConfig.floorGap})`" class="floor-group">
            <text x="-150" y="50" class="floor-title">ІІ поверх</text>
            
            <g :transform="isometricTransform" @click="handleRoomClick" class="floor-plan">
              <path
                d="m 21.143301,21.549903 v 91.078837 l 168.333209,-0.4066 -0.8132,-91.485441 -46.35263,-0.406601 V 66.276119 H 69.935536 l 0.813202,-45.946021 z"
                class="floor-base" 
              />
              <!-- ВСТАВЛЯЄТЕ SVG ДЛЯ 2 ПОВЕРХУ -->


<rect
       style="fill:#ffcc00;stroke-width:0.264583"
       id="room-rect16"
       width="15.315741"
       height="29.730553"
       x="22.823458"
       y="22.823458" />
    <rect
       style="fill:#ffcc00;stroke-width:0.264583"
       id="room-rect17"
       width="16.817284"
       height="24.925617"
       x="22.222839"
       y="54.956482" />
    <rect
       style="fill:#ffcc00;stroke-width:0.264583"
       id="room-rect18"
       width="38.739815"
       height="15.61605"
       x="91.594131"
       y="66.968826" />
    <rect
       style="fill:#ffcc00;stroke-width:0.264583"
       id="room-rect19"
       width="12.012346"
       height="30.631481"
       x="174.77962"
       y="21.321913" />
    <rect
       style="fill:#ffcc00;stroke-width:0.264583"
       id="room-rect20"
       width="12.012346"
       height="22.523148"
       x="175.38025"
       y="55.857407" />
    <rect
       style="fill:#ffcc00;stroke-width:0.264583"
       id="room-rect21"
       width="34.8358"
       height="15.916358"
       x="20.721296"
       y="96.699387" />
    <rect
       style="fill:#ffcc00;stroke-width:0.264583"
       id="room-rect22"
       width="69.971916"
       height="14.715123"
       x="61.863579"
       y="96.999687" />
    <rect
       style="fill:#ffcc00;stroke-width:0.264583"
       id="room-rect23"
       width="45.346607"
       height="16.216667"
       x="141.14507"
       y="96.999687" />

<text
       xml:space="preserve"
       style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#ffcc00;stroke-width:0.264583"
       x="24.367435"
       y="106.19537"
       id="room-text1"
       inkscape:label="Aud3"><tspan
         sodipodi:role="line"
         id="room-tspan1"
         style="fill:#24221c;stroke-width:0.264583"
         x="24.367435"
         y="106.19537">Аудиторія №3</tspan></text>
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#24221c;stroke-width:0.264583"
       x="-85.757759"
       y="31.125608"
       id="room-text2"
       transform="rotate(-91.680856)"
       inkscape:transform-center-x="-0.60061729"
       inkscape:transform-center-y="-0.60061729"
       inkscape:label="aud4"><tspan
         sodipodi:role="line"
         id="room-tspan2"
         style="stroke-width:0.264583"
         x="-85.757759"
         y="31.125608">Аудиторія №4</tspan></text>
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#24221c;stroke-width:0.264583"
       x="-51.500965"
       y="31.000624"
       id="room-text5"
       transform="rotate(-91.680856)"
       inkscape:transform-center-x="-0.60061729"
       inkscape:transform-center-y="-0.60061729"
       inkscape:label="aud4"><tspan
         sodipodi:role="line"
         id="room-tspan5"
         style="stroke-width:0.264583"
         x="-51.500965"
         y="31.000624">Аудиторія №5</tspan></text>
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#24221c;stroke-width:0.264583"
       x="83.241341"
       y="106.00895"
       id="room-text6"><tspan
         sodipodi:role="line"
         id="room-tspan6"
         style="stroke-width:0.264583"
         x="83.241341"
         y="106.00895">Аудиторія №8</tspan></text>
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#24221c;stroke-width:0.264583"
       x="97.241966"
       y="77.179314"
       id="room-text7"><tspan
         sodipodi:role="line"
         id="room-tspan7"
         style="stroke-width:0.264583"
         x="97.241966"
         y="77.179314">Аудиторія №7</tspan></text>
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#24221c;stroke-width:0.264583"
       x="151.29752"
       y="106.60956"
       id="room-text8"><tspan
         sodipodi:role="line"
         id="room-tspan8"
         style="stroke-width:0.264583"
         x="151.29752"
         y="106.60956">Аудиторія №6</tspan></text>
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#24221c;stroke-width:0.264583"
       x="-90.11837"
       y="179.75806"
       id="room-text9"
       transform="rotate(-91.680856)"
       inkscape:transform-center-x="-0.60061729"
       inkscape:transform-center-y="-0.60061729"
       inkscape:label="aud4"><tspan
         sodipodi:role="line"
         id="room-tspan9"
         style="stroke-width:0.264583"
         x="-90.11837"
         y="179.75806">Аудиторія №9</tspan></text>
    <text
       xml:space="preserve"
       style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#24221c;stroke-width:0.264583"
       x="-55.862648"
       y="179.6331"
       id="room-text10"
       transform="rotate(-91.680856)"
       inkscape:transform-center-x="-0.60061729"
       inkscape:transform-center-y="-0.60061729"
       inkscape:label="aud4"><tspan
         sodipodi:role="line"
         id="room-tspan10"
         style="stroke-width:0.264583"
         x="-55.862648"
         y="179.6331">Аудиторія №10</tspan></text>


            </g>
          </g>

          <!-- ========================================== -->
          <!-- ПОВЕРХ 1 -->
          <!-- ========================================== -->
          <g :transform="`translate(0, ${isoConfig.floorGap * 2})`" class="floor-group">
            <text x="-150" y="50" class="floor-title">І поверх</text>
            
            <g :transform="isometricTransform" @click="handleRoomClick" class="floor-plan">
              <path 
                d="m 21.143301,21.549903 v 91.078837 l 168.333209,-0.4066 -0.8132,-91.485441 -46.35263,-0.406601 V 66.276119 H 69.935536 l 0.813202,-45.946021 z"
                class="floor-base" 
              />
              <!-- ВСТАВЛЯЄТЕ SVG ДЛЯ 1 ПОВЕРХУ -->
              
              <rect
                  style="fill:#ffcc00;stroke-width:0.264583"
                  id="room-room-222"
                  width="38.627182"
                  height="17.077282"
                  x="23.17631"
                  y="93.111847"
                  inkscape:label="1p aud 2" />
                <rect
                  style="fill:#ffcc00;stroke-width:0.264583"
                  id="room-room-22"
                  width="23.17631"
                  height="39.033787"
                  x="20.7367"
                  y="37.000778"
                  inkscape:label="1p aud q1" />
                <rect
                  style="fill:#ffcc00;stroke-width:0.264583"
                  id="room-room-конференц зала"
                  width="45.539421"
                  height="17.483883"
                  x="142.31067"
                  y="93.111847"
                  inkscape:label="1p zal" />
                <rect
                    style="fill:#ffd42a;stroke-width:0.264583"
                    id="room-rect15"
                    width="25.929157"
                    height="50.270836"
                    x="162.45418"
                    y="24.341665"
                    ry="0"
                    inkscape:label="root-library" />


               <text
                    xml:space="preserve"
                    style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#f4eed7;stroke-width:0.264583"
                    x="148.5463"
                    y="101.80851"
                    id="room-text12"
                    inkscape:label="konf_zal"><tspan
                      sodipodi:role="line"
                      id="room-tspan12"
                      style="fill:#2b0000;stroke-width:0.264583"
                      x="148.5463"
                      y="101.80851">Конференц. зала</tspan></text>
                  <text
                    xml:space="preserve"
                    transform="scale(0.26458333)"
                    id="room-text13"
                    style="font-weight:bold;font-size:16px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;white-space:pre;shape-inside:url(#rect13);fill:#2b0000"
                    inkscape:label="aud2"><tspan
                      x="108.3125"
                      y="387.25977"
                      id="room-tspan1">Аудиторія №2</tspan></text>
                      <text
       xml:space="preserve"
       style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#24221c;stroke-width:0.264583"
       x="-61.500965"
       y="31.000624"
       id="room-room-text5"
       transform="rotate(-91.680856)"
       inkscape:transform-center-x="-0.60061729"
       inkscape:transform-center-y="-0.60061729"
       inkscape:label="aud4"><tspan
         sodipodi:role="line"
         id="room-tspan5"
         style="stroke-width:0.264583"
         x="-71.500965"
         y="31.000624">Аудиторія №1</tspan></text>
                   <text
                        xml:space="preserve"
                        style="font-weight:bold;font-size:4.23333px;font-family:Roboto;-inkscape-font-specification:'Roboto Bold';writing-mode:lr-tb;direction:ltr;fill:#000000;stroke-width:0.264583"
                        x="165.36459"
                        y="51.32917"
                        id="room-text15"
                          inkscape:label="text-library"><tspan
                            sodipodi:role="line"
                            id="room-tspan15"
                            style="fill:#000000;stroke-width:0.264583"
                            x="165.36459"
                            y="51.32917">Бібліотека</tspan></text>


            </g>
          </g>

        </g>
      </svg>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const selectedRoom = ref(null)

// 1. Реактивний об'єкт з налаштуваннями ізометрії
const isoConfig = ref({
  scaleX: 1.65,
  scaleY: 0.85,
  rotate: -23,
  floorGap: 120 // Відстань між поверхами по осі Y
})

// 2. Обчислювана властивість (computed), яка генерує рядок transform
const isometricTransform = computed(() => {
  return `scale(${isoConfig.value.scaleX}, ${isoConfig.value.scaleY}) rotate(${isoConfig.value.rotate})`
})

// Обробник кліку для всіх поверхів
const handleRoomClick = (event) => {
  const target = event.target
  
  if (target && target.id && target.id.startsWith('room-')) {
    selectedRoom.value = target.id.replace('room-', '')
    
    document.querySelectorAll('.is-active').forEach(el => el.classList.remove('is-active'))
    target.classList.add('is-active')
  }
}
</script>

<style scoped>
.map-container {
  display: flex;
  height: 100vh; /* Змінив на 100vh для зручності */
  background-color: #f4f6f8;
  font-family: sans-serif;
}

.sidebar {
  width: 300px; /* Трохи розширив для повзунків */
  padding: 20px;
  background: white;
  border-right: 1px solid #ddd;
  overflow-y: auto;
}

/* Стилі для панелі керування */
.controls {
  margin-top: 20px;
}
.control-group {
  margin-bottom: 15px;
}
.control-group label {
  display: block;
  font-size: 14px;
  margin-bottom: 5px;
  color: #333;
}
.control-group input[type="range"] {
  width: 100%;
  cursor: pointer;
}

hr {
  border: 0;
  height: 1px;
  background: #ddd;
  margin: 20px 0;
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

.floor-base {
  fill: #e2e8f0;
  stroke: #cbd5e1;
  stroke-width: 2;
  filter: drop-shadow(5px 5px 0px #94a3b8);
}

.room-shape {
  fill: #bae6fd;
  stroke: #ffffff;
  stroke-width: 3;
  cursor: pointer;
  transition: all 0.3s ease;
}

.room-shape:hover {
  fill: #7dd3fc;
  transform: translate(-3px, -3px);
  filter: drop-shadow(3px 3px 2px rgba(0,0,0,0.2));
}

.room-shape.is-active {
  fill: #f59e0b;
  stroke: #b45309;
  stroke-width: 4;
}
</style>