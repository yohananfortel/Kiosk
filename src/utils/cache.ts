/**
 * Утиліта кешування для інформаційного кіоску.
 * Забезпечує офлайн-роботу та швидке завантаження даних за рахунок збереження
 * останніх успішних відповідей API у localStorage.
 */

interface CacheEntry<T> {
  data: T;
  timestamp: number;
  ttl: number;
}

const CACHE_PREFIX = "kiosk_cache_";
const DEFAULT_TTL = 1000 * 60 * 60; // 1 година за замовчуванням

/**
 * Отримати закешовані дані за ключем.
 */
export function getCachedData<T>(key: string, ignoreExpiry = false): T | null {
  try {
    const raw = localStorage.getItem(`${CACHE_PREFIX}${key}`);
    if (!raw) return null;

    const entry: CacheEntry<T> = JSON.parse(raw);
    const isExpired = Date.now() - entry.timestamp > entry.ttl;

    // Якщо не ігноруємо термін дії і кеш застарів - повертаємо null
    if (isExpired && !ignoreExpiry) {
      return null;
    }

    return entry.data;
  } catch (err) {
    console.warn(`[Cache] Помилка читання кешу для "${key}":`, err);
    return null;
  }
}

/**
 * Зберегти дані в кеш.
 */
export function setCachedData<T>(key: string, data: T, ttl = DEFAULT_TTL): void {
  try {
    const entry: CacheEntry<T> = {
      data,
      timestamp: Date.now(),
      ttl,
    };
    localStorage.setItem(`${CACHE_PREFIX}${key}`, JSON.stringify(entry));
  } catch (err) {
    console.warn(`[Cache] Помилка запису в кеш для "${key}":`, err);
  }
}

/**
 * Завантажує дані з API із кешуванням та автоматичним відновленням з офлайн-кешу.
 *
 * Стратегія:
 * 1. Пробує виконати мережевий запит.
 * 2. У разі успіху зберігає результат у localStorage та повертає свіжі дані.
 * 3. У разі помилки мережі (офлайн/збій сервера) повертає закешовані дані, якщо вони є.
 * 4. Якщо кешу немає і запит не вдався - викидає помилку.
 */
export async function fetchWithCache<T>(
  url: string,
  options?: RequestInit,
  ttl = DEFAULT_TTL,
): Promise<T> {
  const cacheKey = url;

  try {
    const response = await fetch(url, options);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    const data: T = await response.json();
    setCachedData(cacheKey, data, ttl);
    return data;
  } catch (networkError) {
    console.warn(
      `[Cache] Мережевий запит до "${url}" не вдався. Спроба завантажити з локального кешу...`,
      networkError,
    );

    // Спроба віддати збережений кеш (навіть якщо він протермінований)
    const fallbackData = getCachedData<T>(cacheKey, true);
    if (fallbackData !== null) {
      console.info(`[Cache] Успішно відновлено дані для "${url}" з офлайн-кешу.`);
      return fallbackData;
    }

    throw networkError;
  }
}

/**
 * Очистити весь кеш кіоску.
 */
export function clearKioskCache(): void {
  try {
    const keysToRemove: string[] = [];
    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i);
      if (key && key.startsWith(CACHE_PREFIX)) {
        keysToRemove.push(key);
      }
    }
    keysToRemove.forEach((k) => localStorage.removeItem(k));
    console.info(`[Cache] Очищено ${keysToRemove.length} записів кешу.`);
  } catch (err) {
    console.warn("[Cache] Помилка очищення кешу:", err);
  }
}
