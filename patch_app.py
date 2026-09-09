with open('/Users/admin/Desktop/робота/Kiosk/src/App.vue', 'r') as f:
    content = f.read()

# 1. Update variables
old_vars = """const idleTimeout = ref(null);
const IDLE_TIME = 90000; // 90 секунд бездіяльності до повернення на головну"""

new_vars = """const idleTimeout = ref(null);
const IDLE_TIME = 25000; // 25 секунд бездіяльності до появи вікна
const COUNTDOWN_TIME = 10; // 10 секунд на підтвердження

const showInactivityModal = ref(false);
const countdown = ref(COUNTDOWN_TIME);
let countdownInterval = null;"""

content = content.replace(old_vars, new_vars)

# 2. Update resetIdleTimer
old_reset = """const resetIdleTimer = () => {
  if (idleTimeout.value) clearTimeout(idleTimeout.value);

  idleTimeout.value = setTimeout(() => {
    // При таймауті:
    // 1. Повертаємося на головний екран
    currentPage.value = 1;
    // 2. Закриваємо відкриті модалки
    if (welcomeRef.value?.closeModal) welcomeRef.value.closeModal();
    if (campaignRef.value?.closeModal) campaignRef.value.closeModal();
  }, IDLE_TIME);
};"""

new_reset = """const resetIdleTimer = () => {
  if (showInactivityModal.value) return;

  if (idleTimeout.value) clearTimeout(idleTimeout.value);

  idleTimeout.value = setTimeout(() => {
    triggerInactivityModal();
  }, IDLE_TIME);
};

const triggerInactivityModal = () => {
  showInactivityModal.value = true;
  countdown.value = COUNTDOWN_TIME;
  
  if (countdownInterval) clearInterval(countdownInterval);
  
  countdownInterval = setInterval(() => {
    countdown.value--;
    if (countdown.value <= 0) {
      clearInterval(countdownInterval);
      handleInactivityTimeout();
    }
  }, 1000);
};

const handleInactivityTimeout = () => {
  showInactivityModal.value = false;
  currentPage.value = 1;
  if (welcomeRef.value?.closeModal) welcomeRef.value.closeModal();
  if (campaignRef.value?.closeModal) campaignRef.value.closeModal();
  resetIdleTimer();
};

const confirmPresence = () => {
  showInactivityModal.value = false;
  if (countdownInterval) clearInterval(countdownInterval);
  resetIdleTimer();
};"""

content = content.replace(old_reset, new_reset)

# 3. Update handleTouchStart & handleTouchEnd
old_touch_start = """const handleTouchStart = (e) => {
  touchStartX.value = e.changedTouches[0].screenX;
  touchStartY.value = e.changedTouches[0].screenY;
  resetIdleTimer();
};"""
new_touch_start = """const handleTouchStart = (e) => {
  if (showInactivityModal.value) return;
  touchStartX.value = e.changedTouches[0].screenX;
  touchStartY.value = e.changedTouches[0].screenY;
  resetIdleTimer();
};"""
content = content.replace(old_touch_start, new_touch_start)

old_touch_end = """const handleTouchEnd = (e) => {
  touchEndX.value = e.changedTouches[0].screenX;
  touchEndY.value = e.changedTouches[0].screenY;
  handleSwipe();
};"""
new_touch_end = """const handleTouchEnd = (e) => {
  if (showInactivityModal.value) return;
  touchEndX.value = e.changedTouches[0].screenX;
  touchEndY.value = e.changedTouches[0].screenY;
  handleSwipe();
};"""
content = content.replace(old_touch_end, new_touch_end)

# 4. Add unmounted interval cleanup
unmounted_old = """onUnmounted(() => {
  if (idleTimeout.value) clearTimeout(idleTimeout.value);"""
unmounted_new = """onUnmounted(() => {
  if (idleTimeout.value) clearTimeout(idleTimeout.value);
  if (countdownInterval) clearInterval(countdownInterval);"""
content = content.replace(unmounted_old, unmounted_new)

# 5. Add template modal
template_dots = """    <div class="kiosk__dots">"""
template_modal = """    <!-- Вікно неактивності -->
    <Transition name="fade">
      <div v-if="showInactivityModal" class="inactivity-modal">
        <div class="inactivity-modal__content">
          <h2 class="inactivity-modal__title">Ви ще тут?</h2>
          <p class="inactivity-modal__text">Повернення на головний екран через <strong>{{ countdown }}</strong> сек.</p>
          <button class="inactivity-modal__btn" @click="confirmPresence">Так, я тут</button>
        </div>
      </div>
    </Transition>

    <div class="kiosk__dots">"""
content = content.replace(template_dots, template_modal)

# 6. Add CSS
css_fade = """.fade-enter-active,
.fade-leave-active {"""
css_modal = """/* ==========================================================================
   Вікно неактивності
   ========================================================================== */
.inactivity-modal {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(6, 78, 59, 0.85);
  backdrop-filter: blur(8px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.inactivity-modal__content {
  background: #ffffff;
  padding: 50px 70px;
  border-radius: 24px;
  text-align: center;
  box-shadow: 0 20px 50px rgba(0,0,0,0.3);
  max-width: 600px;
}

.inactivity-modal__title {
  font-size: 3rem;
  color: #064e3b;
  margin-bottom: 20px;
  font-weight: 800;
}

.inactivity-modal__text {
  font-size: 1.8rem;
  color: #334155;
  margin-bottom: 40px;
}

.inactivity-modal__text strong {
  color: #e11d48;
  font-size: 2.2rem;
}

.inactivity-modal__btn {
  background-color: #00a53f;
  color: white;
  border: none;
  padding: 20px 50px;
  font-size: 2rem;
  font-weight: 700;
  border-radius: 16px;
  cursor: pointer;
  transition: transform 0.2s, background-color 0.2s;
  box-shadow: 0 8px 20px rgba(0, 165, 63, 0.3);
}

.inactivity-modal__btn:active {
  transform: scale(0.95);
  background-color: #008f36;
}

.fade-enter-active,
.fade-leave-active {"""
content = content.replace(css_fade, css_modal)

with open('/Users/admin/Desktop/робота/Kiosk/src/App.vue', 'w') as f:
    f.write(content)

print("Replacement script generated string. Final length:", len(content))
