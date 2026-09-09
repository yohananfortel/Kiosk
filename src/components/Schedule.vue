<template>
  <div class="schedule">
    <!-- Шапка з назвою, годинником та кнопкою оновлення (БЕЗ ЕМОДЗІ) -->
    <header class="schedule__header">
      <div class="schedule__brand">
        <h2 class="schedule__title">Розклад занять</h2>
        <span class="schedule__badge">ВСП «Охтирський фаховий коледж СНАУ»</span>
      </div>

      <div class="schedule__info-bar">
        <div class="schedule__clock">
          <svg class="schedule__clock-svg" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10" />
            <polyline points="12 6 12 12 16 14" />
          </svg>
          <div class="schedule__clock-details">
            <span class="schedule__time">{{ currentTimeDisplay }}</span>
            <span class="schedule__date">{{ currentDateDisplay }}</span>
          </div>
        </div>

        <button
          class="schedule__refresh-btn"
          :disabled="loading"
          title="Оновити розклад"
          @click="fetchData(true)"
        >
          <svg
            class="schedule__refresh-svg"
            :class="{ 'schedule__refresh-svg--spin': loading }"
            viewBox="0 0 24 24"
            width="18"
            height="18"
            fill="none"
            stroke="currentColor"
            stroke-width="2.5"
          >
            <path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67" />
          </svg>
          <span class="schedule__refresh-text">Оновити</span>
        </button>
      </div>
    </header>

    <!-- Панель керування: Вибір групи, курсу, дня та перемикач режимів -->
    <section class="schedule__toolbar">
      <div class="schedule__filter-group">
        <!-- Випадаючий список груп (за замовчуванням "Усі групи") -->
        <div class="schedule__field">
          <label class="schedule__label">Група:</label>
          <div class="schedule__select-box">
            <select
              v-model="selectedGroup"
              class="schedule__select schedule__select--group"
            >
              <option value="all">Усі групи</option>
              <option
                v-for="group in availableGroups"
                :key="group"
                :value="group"
              >
                Група {{ group }}
              </option>
            </select>
          </div>
        </div>

        <!-- Фільтри за курсами (якщо курси визначені) -->
        <div v-if="courses.length > 0" class="schedule__course-chips">
          <button
            type="button"
            class="schedule__chip"
            :class="{ 'schedule__chip--active': selectedCourse === 'all' }"
            @click="selectedCourse = 'all'"
          >
            Всі курси
          </button>
          <button
            v-for="c in courses"
            :key="c"
            type="button"
            class="schedule__chip"
            :class="{ 'schedule__chip--active': selectedCourse === c }"
            @click="selectedCourse = c"
          >
            {{ c }} курс
          </button>
        </div>
      </div>

      <!-- Перемикач режиму відображення: Картки vs Таблиця -->
      <div class="schedule__view-switcher">
        <button
          type="button"
          class="schedule__switch-btn"
          :class="{ 'schedule__switch-btn--active': viewMode === 'cards' }"
          @click="viewMode = 'cards'"
        >
          Картки розкладу
        </button>
        <button
          type="button"
          class="schedule__switch-btn"
          :class="{ 'schedule__switch-btn--active': viewMode === 'table' }"
          @click="viewMode = 'table'"
        >
          Зведена таблиця
        </button>
      </div>
    </section>

    <!-- Стан: Завантаження -->
    <div v-if="loading && scheduleData.length === 0" class="schedule__status schedule__status--loading">
      <div class="schedule__spinner"></div>
      <p class="schedule__status-text">Завантаження та обробка розкладу занять...</p>
    </div>

    <!-- Стан: Помилка -->
    <div v-else-if="error && scheduleData.length === 0" class="schedule__status schedule__status--error">
      <svg class="schedule__error-svg" viewBox="0 0 24 24" width="40" height="40" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z" />
        <line x1="12" y1="9" x2="12" y2="13" />
        <line x1="12" y1="17" x2="12.01" y2="17" />
      </svg>
      <p class="schedule__status-text">{{ error }}</p>
      <button class="schedule__retry-btn" @click="fetchData(true)">Спробувати знову</button>
    </div>

    <!-- Основний вміст -->
    <main v-else class="schedule__main">
      <!-- Вкладки вибору дня тижня -->
      <nav class="schedule-tabs" aria-label="Вибір дня тижня">
        <button
          v-for="day in workDays"
          :key="day"
          type="button"
          class="schedule-tabs__tab"
          :class="{
            'schedule-tabs__tab--active': selectedDay === day,
            'schedule-tabs__tab--today': currentDayName === day
          }"
          @click="selectedDay = day"
        >
          <span class="schedule-tabs__name">{{ day }}</span>
          <span v-if="currentDayName === day" class="schedule-tabs__indicator">Сьогодні</span>
          <span v-else-if="isWeekend && day === 'Понеділок'" class="schedule-tabs__sub">Найближчий</span>
        </button>

        <button
          v-if="selectedGroup !== 'all'"
          type="button"
          class="schedule-tabs__tab schedule-tabs__tab--all"
          :class="{ 'schedule-tabs__tab--active': selectedDay === 'all' }"
          @click="selectedDay = 'all'"
        >
          <span class="schedule-tabs__name">Весь тиждень</span>
        </button>
      </nav>

      <!-- ===================================================================
           ВАРІАНТ 1: ЗА ЗАМОВЧУВАННЯМ — ВСІ ГРУПИ ТА ЇХНІЙ РОЗКЛАД
           =================================================================== -->
      <div v-if="viewMode === 'cards' && selectedGroup === 'all'" class="schedule-all-groups">
        <div class="schedule-all-groups__banner">
          <div class="schedule-all-groups__info">
            <span class="schedule-all-groups__label">Розклад усіх груп на:</span>
            <span class="schedule-all-groups__day-name">{{ activeDayTitle }}</span>
          </div>

          <div class="schedule-all-groups__counter">
            Показано груп: <strong>{{ displayGroups.length }}</strong>
          </div>
        </div>

        <!-- Сітка карток для кожної групи -->
        <div class="groups-grid">
          <div
            v-for="group in displayGroups"
            :key="group"
            class="group-schedule-card"
          >
            <!-- Шапка картки групи -->
            <div class="group-schedule-card__header">
              <h3 class="group-schedule-card__title">Група {{ group }}</h3>
              <button
                type="button"
                class="group-schedule-card__select-btn"
                title="Переглянути детальний розклад цієї групи"
                @click="selectedGroup = group"
              >
                Тільки ця група →
              </button>
            </div>

            <!-- Список 5 пар на цей день -->
            <div class="group-schedule-card__lessons">
              <div
                v-for="para in lessonsPerDay"
                :key="para"
                class="group-lesson-row"
                :class="{
                  'group-lesson-row--active': isActiveLesson(effectiveDayName, para),
                  'group-lesson-row--empty': !getLesson(effectiveDayName, para, group).subject,
                  'group-lesson-row--replacement': getLesson(effectiveDayName, para, group).isReplacement
                }"
              >
                <div class="group-lesson-row__time-col">
                  <span class="group-lesson-row__para">{{ para }} пара</span>
                  <span class="group-lesson-row__time">{{ timeTab[para - 1]?.[0] }}</span>
                  <span
                    v-if="isActiveLesson(effectiveDayName, para)"
                    class="group-lesson-row__live-badge"
                  >
                    Зараз
                  </span>
                </div>

                <div class="group-lesson-row__info-col">
                  <template v-if="getLesson(effectiveDayName, para, group).subject">
                    <div class="group-lesson-row__subject">
                      {{ getLesson(effectiveDayName, para, group).subject }}
                    </div>
                    <div
                      v-if="getLesson(effectiveDayName, para, group).teacher"
                      class="group-lesson-row__teacher"
                    >
                      {{ getLesson(effectiveDayName, para, group).teacher }}
                    </div>
                    <span
                      v-if="getLesson(effectiveDayName, para, group).isReplacement"
                      class="group-lesson-row__replace-tag"
                    >
                      Заміна
                    </span>
                  </template>
                  <div v-else class="group-lesson-row__empty">—</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ===================================================================
           ВАРІАНТ 2: РОЗКЛАД КОНКРЕТНОЇ ОБРАНОЇ ГРУПИ
           =================================================================== -->
      <div v-else-if="viewMode === 'cards' && selectedGroup !== 'all'" class="schedule-single-group">
        <div class="schedule-single-group__banner">
          <div class="schedule-single-group__target">
            <span class="schedule-single-group__label">Група:</span>
            <span class="schedule-single-group__group-name">{{ selectedGroup }}</span>
            <button
              type="button"
              class="schedule-single-group__back-btn"
              @click="selectedGroup = 'all'"
            >
              ← Показати всі групи
            </button>
          </div>

          <div class="schedule-single-group__day-info">
            <span class="schedule-single-group__day-name">{{ activeDayTitle }}</span>
            <span v-if="selectedDay === currentDayName && !isWeekend" class="schedule-single-group__badge-live">
              Зараз у коледжі
            </span>
          </div>
        </div>

        <!-- Денний вигляд для однієї групи (5 великих карток) -->
        <div v-if="selectedDay !== 'all'" class="schedule-cards-list">
          <article
            v-for="para in lessonsPerDay"
            :key="para"
            class="lesson-card"
            :class="{
              'lesson-card--active': isActiveLesson(effectiveDayName, para),
              'lesson-card--empty': !getLesson(effectiveDayName, para, selectedGroup).subject,
              'lesson-card--replacement': getLesson(effectiveDayName, para, selectedGroup).isReplacement
            }"
          >
            <div class="lesson-card__meta">
              <div class="lesson-card__num">{{ para }} пара</div>
              <div class="lesson-card__time">{{ timeTab[para - 1]?.join(' - ') }}</div>
              <div v-if="isActiveLesson(effectiveDayName, para)" class="lesson-card__badge-live">
                <span class="lesson-card__live-dot"></span>
                Зараз іде
              </div>
            </div>

            <div class="lesson-card__details">
              <template v-if="getLesson(effectiveDayName, para, selectedGroup).subject">
                <div class="lesson-card__header">
                  <h3 class="lesson-card__subject">
                    {{ getLesson(effectiveDayName, para, selectedGroup).subject }}
                  </h3>
                  <span
                    v-if="getLesson(effectiveDayName, para, selectedGroup).isReplacement"
                    class="lesson-card__badge-replace"
                  >
                    Заміна
                  </span>
                </div>

                <div
                  v-if="getLesson(effectiveDayName, para, selectedGroup).teacher"
                  class="lesson-card__teacher-row"
                >
                  <span class="lesson-card__teacher-label">Викладач:</span>
                  <span class="lesson-card__teacher-name">
                    {{ getLesson(effectiveDayName, para, selectedGroup).teacher }}
                  </span>
                </div>
              </template>

              <div v-else class="lesson-card__empty-state">
                <span class="lesson-card__empty-text">Занять немає (вікно)</span>
              </div>
            </div>
          </article>
        </div>

        <!-- Тижневий вигляд для однієї групи (5 колонок) -->
        <div v-else class="schedule-week-grid">
          <div
            v-for="day in workDays"
            :key="day"
            class="week-column"
            :class="{ 'week-column--today': currentDayName === day }"
          >
            <div class="week-column__header">
              <h3 class="week-column__title">{{ day }}</h3>
              <span v-if="currentDayName === day" class="week-column__badge-today">Сьогодні</span>
            </div>

            <div class="week-column__lessons">
              <div
                v-for="para in lessonsPerDay"
                :key="para"
                class="week-lesson"
                :class="{
                  'week-lesson--active': isActiveLesson(day, para),
                  'week-lesson--empty': !getLesson(day, para, selectedGroup).subject,
                  'week-lesson--replacement': getLesson(day, para, selectedGroup).isReplacement
                }"
              >
                <div class="week-lesson__top">
                  <span class="week-lesson__num">{{ para }} пара</span>
                  <span class="week-lesson__time">{{ timeTab[para - 1]?.[0] }}</span>
                </div>

                <div v-if="getLesson(day, para, selectedGroup).subject" class="week-lesson__body">
                  <div class="week-lesson__subject">
                    {{ getLesson(day, para, selectedGroup).subject }}
                  </div>
                  <div v-if="getLesson(day, para, selectedGroup).teacher" class="week-lesson__teacher">
                    {{ getLesson(day, para, selectedGroup).teacher }}
                  </div>
                  <span
                    v-if="getLesson(day, para, selectedGroup).isReplacement"
                    class="week-lesson__tag-replace"
                  >
                    Заміна
                  </span>
                </div>
                <div v-else class="week-lesson__empty">—</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ===================================================================
           ВАРІАНТ 3: ЗВЕДЕНА ТАБЛИЦЯ (Для повної деталізації)
           =================================================================== -->
      <div v-else class="schedule-table-view">
        <div class="schedule-table-wrap">
          <table class="schedule-table">
            <thead>
              <tr class="schedule-table__row schedule-table__row--head">
                <th class="schedule-table__th schedule-table__th--day">День</th>
                <th class="schedule-table__th schedule-table__th--num">№</th>
                <th class="schedule-table__th schedule-table__th--time">Час</th>
                <th
                  v-for="group in tableGroups"
                  :key="group"
                  class="schedule-table__th schedule-table__th--group"
                  :class="{ 'schedule-table__th--selected': group === selectedGroup }"
                >
                  Група {{ group }}
                </th>
              </tr>
            </thead>
            <tbody>
              <template v-for="day in workDays" :key="day">
                <tr
                  v-for="para in lessonsPerDay"
                  :key="`${day}-${para}`"
                  class="schedule-table__row"
                  :class="{
                    'schedule-table__row--today': currentDayName === day,
                    'schedule-table__row--active': isActiveLesson(day, para),
                  }"
                >
                  <td v-if="para === 1" :rowspan="lessonsPerDay" class="schedule-table__day-cell">
                    {{ day }}
                  </td>

                  <td class="schedule-table__num-cell">{{ para }}</td>
                  <td class="schedule-table__time-cell">{{ timeTab[para - 1]?.join(' - ') }}</td>

                  <td
                    v-for="group in tableGroups"
                    :key="group"
                    class="schedule-table__lesson-cell"
                    :class="{ 'schedule-table__lesson-cell--selected': group === selectedGroup }"
                  >
                    <div class="schedule-table__lesson-content">
                      <span class="schedule-table__subject">
                        {{ getLesson(day, para, group).subject || '—' }}
                      </span>
                      <span
                        v-if="getLesson(day, para, group).teacher"
                        class="schedule-table__teacher"
                      >
                        {{ getLesson(day, para, group).teacher }}
                      </span>
                      <span
                        v-if="getLesson(day, para, group).isReplacement"
                        class="schedule-table__replacement"
                      >
                        Заміна
                      </span>
                    </div>
                  </td>
                </tr>
              </template>
            </tbody>
          </table>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue';
import * as XLSX from 'xlsx';
import { getCachedData, setCachedData, fetchWithCache } from '../utils/cache';

// --- Константи ---
const daysInWeek = ["Неділя", "Понеділок", "Вівторок", "Середа", "Четвер", "Пʼятниця", "Субота"];
const workDays = ["Понеділок", "Вівторок", "Середа", "Четвер", "Пʼятниця"];

const timeTab = [
  ["08:00", "09:20"],
  ["09:30", "10:50"],
  ["11:35", "12:55"],
  ["13:05", "14:25"],
  ["14:30", "16:00"]
];
const lessonsPerDay = 5;

// --- Стан компонента ---
const currentTime = ref(new Date());
const scheduleData = ref([]);
const teachersLinks = ref({});
const replacements = ref([]);
const groups = ref([]);

// Визначення початкового дня (якщо сьогодні робочий день — беремо його, якщо вихідний — понеділок)
const getDefaultDay = () => {
  const day = new Date().getDay();
  if (day >= 1 && day <= 5) {
    return daysInWeek[day];
  }
  return "Понеділок";
};

// ЗА ЗАМОВЧУВАННЯМ: показувати всі групи та поточний день!
const selectedGroup = ref('all');
const selectedCourse = ref('all');
const selectedDay = ref(getDefaultDay()); // автоматично встановлює поточний день (наприклад, "Середа")
const viewMode = ref('cards'); // 'cards' або 'table'
const loading = ref(true);
const error = ref(null);

// --- Комп'ютед для дат та часу ---
const currentTimeDisplay = computed(() =>
  currentTime.value.toLocaleTimeString('uk-UA', { hour: '2-digit', minute: '2-digit', second: '2-digit' })
);

const currentDateDisplay = computed(() =>
  currentTime.value.toLocaleDateString('uk-UA', { weekday: 'long', day: 'numeric', month: 'long' })
);

const currentDayName = computed(() => {
  const day = currentTime.value.getDay();
  return daysInWeek[day];
});

const isWeekend = computed(() => {
  const day = currentTime.value.getDay();
  return day === 0 || day === 6;
});

// Ефективний день для отримання розкладу
const effectiveDayName = computed(() => {
  if (selectedDay.value === 'all') {
    return isWeekend.value ? "Понеділок" : currentDayName.value;
  }
  return selectedDay.value;
});

const activeDayTitle = computed(() => {
  if (selectedDay.value === 'all') {
    return "Весь навчальний тиждень";
  }
  if (selectedDay.value === currentDayName.value && !isWeekend.value) {
    return `${selectedDay.value} (сьогодні)`;
  }
  if (isWeekend.value && selectedDay.value === "Понеділок") {
    return "Понеділок (найближчий навчальний день)";
  }
  return selectedDay.value;
});

// Список курсів на основі назв груп (наприклад 11-А -> 1 курс)
const courses = computed(() => {
  const set = new Set();
  groups.value.forEach(g => {
    const match = String(g).trim().match(/^(\d)/);
    if (match) set.add(match[1]);
  });
  return Array.from(set).sort();
});

// Доступні групи відповідно до обраного курсу
const availableGroups = computed(() => {
  if (selectedCourse.value === 'all') return groups.value;
  return groups.value.filter(g => String(g).trim().startsWith(selectedCourse.value));
});

// Групи для відображення карток
const displayGroups = computed(() => {
  return availableGroups.value.length > 0 ? availableGroups.value : groups.value;
});

// Групи для зведеної таблиці
const tableGroups = computed(() => {
  if (selectedGroup.value !== 'all') return [selectedGroup.value];
  return displayGroups.value;
});

// --- Допоміжні функції уроків ---
const isActiveLesson = (dayName, paraIndex) => {
  if (currentDayName.value !== dayName || isWeekend.value) return false;

  const now = currentTime.value.getHours() * 60 + currentTime.value.getMinutes();
  const slot = timeTab[paraIndex - 1];
  if (!slot) return false;

  const [startH, startM] = slot[0].split(':').map(Number);
  const [endH, endM] = slot[1].split(':').map(Number);
  const start = startH * 60 + startM;
  const end = endH * 60 + endM;

  return now >= start && now <= end;
};

const getLesson = (dayName, para, groupName) => {
  if (!scheduleData.value || scheduleData.value.length === 0 || !groupName) {
    return { subject: '', teacher: '', isReplacement: false };
  }

  const dayIdx = daysInWeek.indexOf(dayName);
  if (dayIdx < 1 || dayIdx > 5) {
    return { subject: '', teacher: '', isReplacement: false };
  }

  const rowIndex = ((dayIdx - 1) * lessonsPerDay * 2) + ((para - 1) * 2) + 1;
  const headerRow = scheduleData.value[0] || [];
  const colIndex = headerRow.indexOf(groupName);

  if (colIndex === -1) {
    return { subject: '', teacher: '', isReplacement: false };
  }

  let subject = String(scheduleData.value[rowIndex]?.[colIndex] || '').trim();
  let teacher = String(scheduleData.value[rowIndex + 1]?.[colIndex] || '').trim();
  let isReplacement = false;

  const replacement = replacements.value.find(r =>
    r.group === groupName &&
    Number(r.para) === para &&
    daysInWeek[r.day] === dayName
  );

  if (replacement) {
    subject = replacement.discip || subject;
    teacher = replacement.teacher || teacher;
    isReplacement = true;
  }

  return { subject, teacher, isReplacement };
};

// URL з проксі для дев-сервера
const getEndpointUrl = (path) => {
  if (import.meta.env.DEV) {
    return `/api-ocsnau${path}`;
  }
  return `https://ocsnau.net${path}`;
};

// --- Завантаження розкладу ---
const fetchData = async (forceRefresh = false) => {
  try {
    loading.value = true;
    error.value = null;

    // 1. Відновлення з локального кешу
    if (!forceRefresh) {
      const cachedSchedule = getCachedData('parsed_schedule', true);
      const cachedGroups = getCachedData('parsed_groups', true);
      if (cachedSchedule && cachedGroups && cachedGroups.length > 0) {
        scheduleData.value = cachedSchedule;
        groups.value = cachedGroups;
      }
    }

    // 2. Викладачі з кешуванням
    try {
      const teachersUrl = getEndpointUrl('/shedule-data/data.json');
      teachersLinks.value = await fetchWithCache(teachersUrl, {}, 1000 * 60 * 60 * 24);
    } catch {
      console.warn('[Schedule] Не вдалося оновити список викладачів');
    }

    // 3. Завантаження Excel файлу розкладу
    const excelPath = '/wp-content/uploads/2026/02/rozklad-na_ii-semestr-2025-2026-n.r.-14.01-2.xls';
    let eResp;
    try {
      eResp = await fetch(getEndpointUrl(excelPath));
    } catch {
      console.warn('[Schedule] Спроба через резервний проксі...');
      const fallbackUrl = `https://api.allorigins.win/raw?url=${encodeURIComponent('https://ocsnau.net' + excelPath)}`;
      eResp = await fetch(fallbackUrl);
    }

    if (!eResp || !eResp.ok) throw new Error('Не вдалося завантажити файл розкладу');

    const arrayBuffer = await eResp.arrayBuffer();
    const workbook = XLSX.read(arrayBuffer, { type: 'array' });
    const firstSheet = workbook.Sheets[workbook.SheetNames[0]];
    const rawData = XLSX.utils.sheet_to_json(firstSheet, { header: 1 });

    if (rawData && rawData.length > 0) {
      scheduleData.value = rawData;
      const parsedGroups = Array.from(new Set(rawData[0].slice(1).filter(Boolean)));
      groups.value = parsedGroups;

      setCachedData('parsed_schedule', scheduleData.value, 1000 * 60 * 60 * 6);
      setCachedData('parsed_groups', groups.value, 1000 * 60 * 60 * 6);
    }
  } catch (err) {
    if (scheduleData.value.length === 0) {
      error.value = "Не вдалося завантажити розклад. Будь ласка, перевірте зв'язок з інтернетом.";
    }
    console.error('[Schedule] Помилка завантаження:', err);
  } finally {
    loading.value = false;
  }
};

let clockInterval;
let autoRefreshInterval;

onMounted(() => {
  fetchData();
  clockInterval = setInterval(() => {
    currentTime.value = new Date();
  }, 1000);

  // Оновлення кожні 15 хвилин
  autoRefreshInterval = setInterval(() => fetchData(true), 900000);
});

onUnmounted(() => {
  if (clockInterval) clearInterval(clockInterval);
  if (autoRefreshInterval) clearInterval(autoRefreshInterval);
});
</script>

<style scoped>
/* ==========================================================================
   Блок: schedule (Розклад занять кіоску)
   Стиль: чистий, професійний, без емодзі
   ========================================================================== */

.schedule {
  display: flex;
  flex-direction: column;
  width: 100%;
  min-height: 100%;
  padding: 10px 15px 30px;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: #0f172a;
  background-color: #ffffff;
  border-radius: 24px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}

/* --------------------------------------------------------------------------
   Шапка (Header)
   -------------------------------------------------------------------------- */

.schedule__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
  padding-bottom: 18px;
  border-bottom: 2px solid #e2e8f0;
  margin-bottom: 20px;
}

.schedule__brand {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.schedule__title {
  font-size: 2.2rem;
  font-weight: 800;
  color: #166534;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0;
  line-height: 1.1;
}

.schedule__badge {
  font-size: 1rem;
  font-weight: 600;
  color: #64748b;
}

.schedule__info-bar {
  display: flex;
  align-items: center;
  gap: 16px;
}

.schedule__clock {
  display: flex;
  align-items: center;
  gap: 12px;
  background: #f0fdf4;
  border: 2px solid #bbf7d0;
  padding: 8px 18px;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(22, 101, 52, 0.05);
}

.schedule__clock-svg {
  color: #166534;
  flex-shrink: 0;
}

.schedule__clock-details {
  display: flex;
  flex-direction: column;
}

.schedule__time {
  font-size: 1.4rem;
  font-weight: 800;
  color: #166534;
  font-variant-numeric: tabular-nums;
  line-height: 1.1;
}

.schedule__date {
  font-size: 0.85rem;
  font-weight: 600;
  color: #475569;
  text-transform: capitalize;
}

.schedule__refresh-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  font-size: 1.05rem;
  font-weight: 700;
  background-color: #166534;
  color: #ffffff;
  border: none;
  border-radius: 14px;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(22, 101, 52, 0.2);
  transition: background-color 0.2s, transform 0.1s;
}

.schedule__refresh-btn:active {
  transform: scale(0.96);
  background-color: #14532d;
}

.schedule__refresh-svg--spin {
  animation: spin 1s linear infinite;
}

/* --------------------------------------------------------------------------
   Панель інструментів (Toolbar)
   -------------------------------------------------------------------------- */

.schedule__toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 20px;
  padding: 16px 22px;
  margin-bottom: 24px;
}

.schedule__filter-group {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;
}

.schedule__field {
  display: flex;
  align-items: center;
  gap: 12px;
}

.schedule__label {
  font-size: 1.25rem;
  font-weight: 800;
  color: #1e293b;
}

.schedule__select-box {
  position: relative;
}

.schedule__select--group {
  min-width: 200px;
  padding: 12px 42px 12px 18px;
  font-size: 1.3rem;
  font-weight: 800;
  color: #166534;
  background-color: #ffffff;
  border-radius: 24px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  border: 2px solid #86efac;
  border-radius: 14px;
  cursor: pointer;
  outline: none;
  appearance: auto;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.04);
  transition: border-color 0.2s, box-shadow 0.2s;
}

.schedule__select--group:focus {
  border-color: #166534;
  box-shadow: 0 0 0 3px rgba(22, 101, 52, 0.15);
}

.schedule__course-chips {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.schedule__chip {
  padding: 8px 16px;
  font-size: 1rem;
  font-weight: 700;
  border: 1px solid #cbd5e1;
  background: #ffffff;
  color: #475569;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s;
}

.schedule__chip:hover {
  background: #f1f5f9;
  border-color: #94a3b8;
}

.schedule__chip--active {
  background: #166534;
  color: #ffffff;
  border-color: #166534;
  box-shadow: 0 4px 10px rgba(22, 101, 52, 0.2);
}

.schedule__view-switcher {
  display: flex;
  background: #e2e8f0;
  padding: 4px;
  border-radius: 14px;
  gap: 4px;
}

.schedule__switch-btn {
  padding: 10px 18px;
  font-size: 1.05rem;
  font-weight: 700;
  border: none;
  border-radius: 10px;
  background: transparent;
  color: #475569;
  cursor: pointer;
  transition: all 0.2s;
}

.schedule__switch-btn--active {
  background: #ffffff;
  color: #166534;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* --------------------------------------------------------------------------
   Статуси завантаження та помилок
   -------------------------------------------------------------------------- */

.schedule__status {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  text-align: center;
  gap: 16px;
}

.schedule__status--loading {
  color: #166534;
}

.schedule__status--error {
  color: #dc2626;
}

.schedule__status-text {
  font-size: 1.3rem;
  font-weight: 700;
  margin: 0;
}

.schedule__spinner {
  width: 54px;
  height: 54px;
  border: 5px solid #e2e8f0;
  border-top-color: #166534;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.schedule__error-svg {
  color: #dc2626;
}

.schedule__retry-btn {
  padding: 12px 28px;
  font-size: 1.15rem;
  font-weight: 700;
  background: #dc2626;
  color: white;
  border: none;
  border-radius: 12px;
  cursor: pointer;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* --------------------------------------------------------------------------
   Вкладки днів тижня (Schedule Tabs)
   -------------------------------------------------------------------------- */

.schedule-tabs {
  display: flex;
  align-items: stretch;
  gap: 10px;
  overflow-x: auto;
  padding-bottom: 8px;
  margin-bottom: 20px;
}

.schedule-tabs__tab {
  flex: 1;
  min-width: 130px;
  padding: 14px 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  background: #f8fafc;
  border: 2px solid #e2e8f0;
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.2s ease;
  user-select: none;
}

.schedule-tabs__tab:hover {
  background: #f1f5f9;
  border-color: #cbd5e1;
}

.schedule-tabs__tab--active {
  background: #166534 !important;
  color: #ffffff !important;
  border-color: #166534 !important;
  box-shadow: 0 8px 18px rgba(22, 101, 52, 0.25);
  transform: translateY(-2px);
}

.schedule-tabs__name {
  font-size: 1.2rem;
  font-weight: 800;
  color: #334155;
}

.schedule-tabs__tab--active .schedule-tabs__name {
  color: #ffffff;
}

.schedule-tabs__sub {
  font-size: 0.85rem;
  font-weight: 600;
  color: #64748b;
}

.schedule-tabs__tab--active .schedule-tabs__sub {
  color: #bbf7d0;
}

.schedule-tabs__indicator {
  font-size: 0.75rem;
  font-weight: 700;
  background: #dcfce7;
  color: #15803d;
  padding: 2px 8px;
  border-radius: 10px;
}

.schedule-tabs__tab--active .schedule-tabs__indicator {
  background: #14532d;
  color: #86efac;
}

.schedule-tabs__tab--all {
  background: #fafaf9;
  border-color: #e7e5e4;
}

/* ==========================================================================
   ВАРІАНТ 1: ВСІ ГРУПИ ТА ЇХ РОЗКЛАД (За замовчуванням)
   ========================================================================== */

.schedule-all-groups {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.schedule-all-groups__banner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  border-radius: 16px;
  padding: 14px 22px;
}

.schedule-all-groups__info {
  display: flex;
  align-items: center;
  gap: 10px;
}

.schedule-all-groups__label {
  font-size: 1.15rem;
  font-weight: 700;
  color: #166534;
}

.schedule-all-groups__day-name {
  font-size: 1.4rem;
  font-weight: 900;
  color: #064e3b;
}

.schedule-all-groups__counter {
  font-size: 1rem;
  font-weight: 600;
  color: #475569;
}

/* Сітка карток груп */
.groups-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 20px;
  width: 100%;
}

.group-schedule-card {
  display: flex;
  flex-direction: column;
  background: #ffffff;
  border: 2px solid #e2e8f0;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
  transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
}

.group-schedule-card:hover {
  border-color: #166534;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
}

.group-schedule-card__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #166534;
  color: #ffffff;
  padding: 12px 18px;
}

.group-schedule-card__title {
  font-size: 1.35rem;
  font-weight: 800;
  margin: 0;
  letter-spacing: 0.3px;
}

.group-schedule-card__select-btn {
  padding: 6px 12px;
  font-size: 0.85rem;
  font-weight: 700;
  background: rgba(255, 255, 255, 0.2);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.4);
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.15s;
}

.group-schedule-card__select-btn:hover {
  background: rgba(255, 255, 255, 0.35);
}

.group-schedule-card__lessons {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 12px;
  flex: 1;
}

.group-lesson-row {
  display: flex;
  align-items: center;
  border: 1px solid #f1f5f9;
  border-radius: 12px;
  padding: 8px 12px;
  gap: 12px;
  background: #ffffff;
}

.group-lesson-row--active {
  background: #f0fdf4;
  border-color: #22c55e;
  box-shadow: 0 0 0 1px #22c55e;
}

.group-lesson-row--replacement {
  border-left: 5px solid #f59e0b;
}

.group-lesson-row--empty {
  background: #f8fafc;
  opacity: 0.65;
}

.group-lesson-row__time-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-width: 60px;
  padding-right: 10px;
  border-right: 1px solid #e2e8f0;
}

.group-lesson-row__para {
  font-size: 0.95rem;
  font-weight: 800;
  color: #166534;
}

.group-lesson-row__time {
  font-size: 0.8rem;
  font-weight: 600;
  color: #64748b;
}

.group-lesson-row__live-badge {
  font-size: 0.65rem;
  font-weight: 800;
  color: #15803d;
  background: #dcfce7;
  padding: 1px 5px;
  border-radius: 6px;
  margin-top: 2px;
}

.group-lesson-row__info-col {
  display: flex;
  flex-direction: column;
  gap: 2px;
  flex: 1;
}

.group-lesson-row__subject {
  font-size: 1.05rem;
  font-weight: 800;
  color: #0f172a;
  line-height: 1.2;
}

.group-lesson-row__teacher {
  font-size: 0.85rem;
  font-weight: 600;
  color: #166534;
}

.group-lesson-row__replace-tag {
  display: inline-block;
  font-size: 0.7rem;
  font-weight: 800;
  color: #b45309;
  background: #fef3c7;
  padding: 1px 5px;
  border-radius: 4px;
  width: fit-content;
}

.group-lesson-row__empty {
  color: #cbd5e1;
  font-weight: 700;
}

/* ==========================================================================
   ВАРІАНТ 2: РОЗКЛАД КОНКРЕТНОЇ ОБРАНОЇ ГРУПИ
   ========================================================================== */

.schedule-single-group {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.schedule-single-group__banner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  border-radius: 16px;
  padding: 14px 22px;
}

.schedule-single-group__target {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.schedule-single-group__label {
  font-size: 1.15rem;
  font-weight: 700;
  color: #166534;
}

.schedule-single-group__group-name {
  font-size: 1.5rem;
  font-weight: 900;
  color: #064e3b;
  background: #ffffff;
  padding: 4px 14px;
  border-radius: 10px;
  border: 1px solid #86efac;
}

.schedule-single-group__back-btn {
  padding: 6px 14px;
  font-size: 0.95rem;
  font-weight: 700;
  background: #ffffff;
  color: #166534;
  border: 1px solid #86efac;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.15s;
}

.schedule-single-group__back-btn:hover {
  background: #e2e8f0;
}

.schedule-single-group__day-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.schedule-single-group__day-name {
  font-size: 1.3rem;
  font-weight: 800;
  color: #1e293b;
}

.schedule-single-group__badge-live {
  font-size: 0.9rem;
  font-weight: 700;
  color: #15803d;
  background: #dcfce7;
  padding: 4px 12px;
  border-radius: 12px;
}

/* Великі картки для одного дня */
.schedule-cards-list {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.lesson-card {
  display: flex;
  align-items: stretch;
  background: #ffffff;
  border: 2px solid #e2e8f0;
  border-radius: 20px;
  padding: 18px 24px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
  transition: all 0.2s ease;
}

.lesson-card:hover {
  border-color: #cbd5e1;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.06);
}

.lesson-card--active {
  background: #f0fdf4;
  border-color: #22c55e;
  box-shadow: 0 8px 25px rgba(34, 197, 94, 0.15);
}

.lesson-card--replacement {
  border-left: 8px solid #f59e0b;
}

.lesson-card--empty {
  background: #f8fafc;
  opacity: 0.85;
  border-style: dashed;
}

.lesson-card__meta {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-width: 140px;
  padding-right: 24px;
  border-right: 2px solid #f1f5f9;
  text-align: center;
}

.lesson-card__num {
  font-size: 1.4rem;
  font-weight: 900;
  color: #166534;
  margin-bottom: 4px;
}

.lesson-card__time {
  font-size: 1.05rem;
  font-weight: 700;
  color: #64748b;
  background: #f1f5f9;
  padding: 4px 10px;
  border-radius: 8px;
}

.lesson-card__badge-live {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: 8px;
  font-size: 0.85rem;
  font-weight: 800;
  color: #15803d;
  background: #dcfce7;
  padding: 3px 10px;
  border-radius: 12px;
}

.lesson-card__live-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: #22c55e;
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }
  70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(34, 197, 94, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
}

.lesson-card__details {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-left: 24px;
  flex: 1;
  gap: 8px;
}

.lesson-card__header {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.lesson-card__subject {
  font-size: 1.55rem;
  font-weight: 800;
  color: #0f172a;
  margin: 0;
  line-height: 1.25;
}

.lesson-card__badge-replace {
  font-size: 0.85rem;
  font-weight: 800;
  color: #b45309;
  background: #fef3c7;
  padding: 3px 10px;
  border-radius: 8px;
}

.lesson-card__teacher-row {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.lesson-card__teacher-label {
  font-size: 1.1rem;
  font-weight: 600;
  color: #64748b;
}

.lesson-card__teacher-name {
  font-size: 1.25rem;
  font-weight: 700;
  color: #166534;
}

.lesson-card__empty-state {
  display: flex;
  align-items: center;
  color: #94a3b8;
}

.lesson-card__empty-text {
  font-size: 1.2rem;
  font-weight: 600;
}

/* Тижнева сітка для 1 групи (5 колонок) */
.schedule-week-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 14px;
  width: 100%;
}

.week-column {
  display: flex;
  flex-direction: column;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 18px;
  overflow: hidden;
}

.week-column--today {
  border: 2px solid #166534;
  background: #f0fdf4;
}

.week-column__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #e2e8f0;
  padding: 12px 14px;
}

.week-column--today .week-column__header {
  background: #166534;
  color: #ffffff;
}

.week-column__title {
  font-size: 1.15rem;
  font-weight: 800;
  margin: 0;
}

.week-column__badge-today {
  font-size: 0.75rem;
  font-weight: 800;
  background: #dcfce7;
  color: #15803d;
  padding: 2px 6px;
  border-radius: 6px;
}

.week-column__lessons {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 10px;
  flex: 1;
}

.week-lesson {
  display: flex;
  flex-direction: column;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 8px 10px;
  gap: 4px;
  min-height: 85px;
}

.week-lesson--active {
  border-color: #22c55e;
  background: #f0fdf4;
}

.week-lesson--empty {
  background: #f8fafc;
  border-style: dashed;
  justify-content: center;
  align-items: center;
}

.week-lesson__top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.8rem;
  font-weight: 700;
  color: #64748b;
  border-bottom: 1px solid #f1f5f9;
  padding-bottom: 2px;
}

.week-lesson__subject {
  font-size: 0.95rem;
  font-weight: 800;
  color: #0f172a;
  line-height: 1.2;
}

.week-lesson__teacher {
  font-size: 0.8rem;
  font-weight: 600;
  color: #166534;
}

.week-lesson__tag-replace {
  display: inline-block;
  font-size: 0.7rem;
  font-weight: 800;
  color: #b45309;
  background: #fef3c7;
  padding: 1px 4px;
  border-radius: 4px;
}

.week-lesson__empty {
  color: #cbd5e1;
  font-weight: 700;
}

/* ==========================================================================
   ВАРІАНТ 3: ЗВЕДЕНА ТАБЛИЦЯ
   ========================================================================== */

.schedule-table-view {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.schedule-table-wrap {
  width: 100%;
  overflow-x: auto;
  max-height: 65vh;
  border: 2px solid #cbd5e1;
  border-radius: 16px;
  background: #ffffff;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}

.schedule-table {
  width: 100%;
  border-collapse: collapse;
  table-layout: auto;
}

.schedule-table__th,
.schedule-table__day-cell,
.schedule-table__num-cell,
.schedule-table__time-cell,
.schedule-table__lesson-cell {
  border: 1px solid #e2e8f0;
  padding: 8px 10px;
  text-align: center;
  vertical-align: middle;
}

.schedule-table__th {
  background-color: #166534;
  color: #ffffff;
  font-weight: 800;
  font-size: 0.95rem;
  position: sticky;
  top: 0;
  z-index: 3;
}

.schedule-table__th--group {
  min-width: 160px;
}

.schedule-table__th--selected {
  background-color: #064e3b;
  border-left: 2px solid #86efac;
  border-right: 2px solid #86efac;
}

.schedule-table__day-cell {
  width: 45px;
  font-weight: 900;
  background-color: #f8fafc;
  color: #166534;
  writing-mode: vertical-rl;
  text-orientation: mixed;
  font-size: 1rem;
}

.schedule-table__num-cell {
  width: 35px;
  font-weight: 800;
  background-color: #f1f5f9;
  font-size: 1rem;
}

.schedule-table__time-cell {
  width: 110px;
  font-size: 0.85rem;
  font-weight: 700;
  color: #475569;
  background-color: #f8fafc;
  white-space: nowrap;
}

.schedule-table__row--today .schedule-table__day-cell {
  background-color: #dcfce7;
  color: #15803d;
}

.schedule-table__row--active {
  background-color: #fef08a !important;
}

.schedule-table__lesson-cell--selected {
  background-color: #f0fdf4;
  border-left: 2px solid #86efac;
  border-right: 2px solid #86efac;
}

.schedule-table__lesson-content {
  display: flex;
  flex-direction: column;
  gap: 4px;
  text-align: left;
  line-height: 1.25;
}

.schedule-table__subject {
  font-weight: 800;
  font-size: 0.95rem;
  color: #0f172a;
}

.schedule-table__teacher {
  font-size: 0.85rem;
  color: #166534;
  font-weight: 600;
}

.schedule-table__replacement {
  display: inline-block;
  font-size: 0.75rem;
  color: #b45309;
  font-weight: 800;
  background: #fef3c7;
  padding: 2px 6px;
  border-radius: 4px;
  width: fit-content;
}
</style>

