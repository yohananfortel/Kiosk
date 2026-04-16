<template>
  <div class="schedule-container">
    <div class="controls">
      <div id="clock" class="clock-display">{{ currentTimeDisplay }}</div>
      
      <select v-model="selectedGroup">
        <option value="all">Усі групи</option>
        <option v-for="group in groups" :key="group" :value="group">{{ group }}</option>
      </select>

      <select v-model="selectedDay">
        <option value="all">Усі дні</option>
        <option v-for="day in daysInWeek.slice(1, 6)" :key="day" :value="day">{{ day }}</option>
      </select>
    </div>

    <div v-if="loading">Завантаження...</div>
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else>
      <div class="table-responsive desktop-only">
        <table class="table table-striped table-bordered">
          <thead>
            <tr>
              <th>День</th>
              <th>№</th>
              <th>Час</th>
              <th v-for="group in filteredGroups" :key="group">{{ group }}</th>
            </tr>
          </thead>
          <tbody>
            <template v-for="day in activeDays" :key="day">
              <tr v-for="para in lessonsPerDay" :key="`${day}-${para}`" 
                  :class="{ 'today': isToday(day), 'active-lesson': isActiveLesson(day, para) }">
                
                <td v-if="para === 1" :rowspan="lessonsPerDay" class="day-cell">{{ day }}</td>
                
                <td>{{ para }}</td>
                <td>{{ timeTab[para - 1].join(' - ') }}</td>
                
                <td v-for="group in filteredGroups" :key="group">
                  <div v-html="getLessonContent(day, para, group)"></div>
                </td>
              </tr>
            </template>
          </tbody>
        </table>
      </div>

      <div class="mobile-only">
        <div v-for="group in filteredGroups" :key="'mob-'+group" class="group-card">
          <h3>{{ group }}</h3>
          <div v-for="day in activeDays" :key="'mob-day-'+day">
            <div class="lesson-day">{{ day }}</div>
            <div v-for="para in lessonsPerDay" :key="'mob-para-'+para" 
                 class="lesson" 
                 :class="{ 'today': isToday(day), 'active-lesson': isActiveLesson(day, para) }">
              <div class="lesson-info">
                <strong>{{ para }}. {{ timeTab[para-1][0] }} - {{ timeTab[para-1][1] }}</strong>
                <div v-html="getLessonContent(day, para, group)"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue';
import * as XLSX from 'xlsx'; // Переконайтеся, що бібліотека встановлена

// --- Константи ---
const daysInWeek = ["Неділя", "Понеділок", "Вівторок", "Середа", "Четвер", "Пʼятниця", "Субота"];
const timeTab = [["08:00", "09:20"], ["09:30", "10:50"], ["11:35", "12:55"], ["13:05", "14:25"], ["14:30", "16:00"]];
const lessonsPerDay = 5;

// --- Стан (Reactive State) ---
const currentTime = ref(new Date());
const scheduleData = ref([]);
const teachersLinks = ref({});
const replacements = ref([]); // Це ваш масив 'correct'
const groups = ref([]);
const selectedGroup = ref('all');
const selectedDay = ref('all');
const loading = ref(true);
const error = ref(null);

// --- Computed ---
const currentTimeDisplay = computed(() => currentTime.value.toLocaleString('uk-UA'));

const filteredGroups = computed(() => {
  return selectedGroup.value === 'all' ? groups.value : [selectedGroup.value];
});

const activeDays = computed(() => {
  if (selectedDay.value !== 'all') return [selectedDay.value];
  return daysInWeek.slice(1, 6); // Понеділок - П'ятниця
});

// --- Функції логіки ---
const isToday = (dayName) => daysInWeek[currentTime.value.getDay()] === dayName;

const isActiveLesson = (dayName, paraIndex) => {
  if (!isToday(dayName)) return false;
  
  const now = currentTime.value.getHours() * 60 + currentTime.value.getMinutes();
  const [start, end] = timeTab[paraIndex - 1].map(t => {
    const [h, m] = t.split(':').map(Number);
    return h * 60 + m;
  });
  return now >= start && now <= end;
};

const getLessonContent = (dayName, para, groupName) => {
  const dayIdx = daysInWeek.indexOf(dayName);
  // Розрахунок індексу рядка в Excel (базуючись на вашій логіці rowIndex += 2)
  const rowIndex = ((dayIdx - 1) * lessonsPerDay * 2) + ((para - 1) * 2) + 1;
  const colIndex = groups.value.indexOf(groupName) + 1;

  let subject = scheduleData.value[rowIndex]?.[colIndex] || '';
  let teacher = scheduleData.value[rowIndex + 1]?.[colIndex] || '';

  // Перевірка замін (replacements)
  const replacement = replacements.value.find(r => 
    r.group === groupName && 
    Number(r.para) === para && 
    daysInWeek[r.day] === dayName
  );

  if (replacement) {
    subject = replacement.discip;
    teacher = replacement.teacher;
  }

  let teacherHtml = teacher ? linkifyTeacher(teacher) : '';
  if (replacement) teacherHtml += '<div class="replacement-label">🔄 Заміна</div>';

  return `${subject}<br>${teacherHtml}`;
};

const linkifyTeacher = (text) => {
  let str = String(text);
  for (const [name, url] of Object.entries(teachersLinks.value)) {
    const regex = new RegExp(name, "g");
    str = str.replace(regex, `<a href="${url}" target="_blank">${name}</a>`);
  }
  return str;
};

// --- Завантаження даних ---
const fetchData = async () => {
  try {
    loading.value = true;
    
    // 1. Завантаження JSON викладачів
    const tResp = await fetch('https://ocsnau.net/shedule-data/data.json');
    teachersLinks.value = await tResp.json();

    // 2. Завантаження Excel
    const eResp = await fetch('https://ocsnau.net/wp-content/uploads/2026/02/rozklad-na_ii-semestr-2025-2026-n.r.-14.01-2.xls'); // ex_she
    const arrayBuffer = await eResp.arrayBuffer();
    const workbook = XLSX.read(arrayBuffer, { type: 'array' });
    const firstSheet = workbook.Sheets[workbook.SheetNames[0]];
    const rawData = XLSX.utils.sheet_to_json(firstSheet, { header: 1 });

    if (rawData.length > 0) {
      scheduleData.value = rawData;
      groups.value = rawData[0].slice(1); // Перший рядок, крім першої колонки
    }
    
    loading.value = false;
  } catch (e) {
    error.value = "Помилка завантаження даних.";
    console.error(e);
  }
};

// --- Таймери ---
let clockInterval, dataInterval;

onMounted(() => {
  fetchData();
  clockInterval = setInterval(() => {
    currentTime.value = new Date();
  }, 1000);

  // Оновлення даних кожні 15 хвилин
  dataInterval = setInterval(fetchData, 900000);
});

onUnmounted(() => {
  clearInterval(clockInterval);
  clearInterval(dataInterval);
});
</script>

<style scoped>
.today { background-color: rgba(255, 235, 59, 0.1); }
.active-lesson { border: 2px solid #4CAF50 !important; font-weight: bold; }
.replacement-label { font-size: 12px; color: #388e3c; }
.day-cell { vertical-align: middle; text-align: center; font-weight: bold; }

@media (max-width: 768px) {
  .desktop-only { display: none; }
}
@media (min-width: 769px) {
  .mobile-only { display: none; }
}
</style>