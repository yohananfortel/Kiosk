with open('/Users/admin/Desktop/робота/Kiosk/src/App.vue', 'r') as f:
    content = f.read()

# 1. Add scheduleRef to script setup
script_vars = """const welcomeRef = ref(null);
const campaignRef = ref(null);"""

script_vars_new = """const scheduleRef = ref(null);
const welcomeRef = ref(null);
const campaignRef = ref(null);"""
content = content.replace(script_vars, script_vars_new)

# 2. Modify triggerInactivityModal
old_trigger = """const triggerInactivityModal = () => {
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
};"""

new_trigger = """const triggerInactivityModal = () => {
  // На першій сторінці (розклад) тихо скидаємо фільтри, без вікна
  if (currentPage.value === 1) {
    if (scheduleRef.value?.resetToDefault) {
      scheduleRef.value.resetToDefault();
    }
    // І починаємо відлік 25с знову
    resetIdleTimer();
    return;
  }

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
};"""
content = content.replace(old_trigger, new_trigger)

# 3. Add ref to Schedule component in template
old_schedule_comp = """<Schedule class="kiosk__page-content" />"""
new_schedule_comp = """<Schedule ref="scheduleRef" class="kiosk__page-content" />"""
content = content.replace(old_schedule_comp, new_schedule_comp)

# Also ensure handleInactivityTimeout resets schedule too when returning from other pages
old_timeout = """const handleInactivityTimeout = () => {
  showInactivityModal.value = false;
  currentPage.value = 1;
  if (welcomeRef.value?.closeModal) welcomeRef.value.closeModal();
  if (campaignRef.value?.closeModal) campaignRef.value.closeModal();
  resetIdleTimer();
};"""

new_timeout = """const handleInactivityTimeout = () => {
  showInactivityModal.value = false;
  currentPage.value = 1;
  if (welcomeRef.value?.closeModal) welcomeRef.value.closeModal();
  if (campaignRef.value?.closeModal) campaignRef.value.closeModal();
  if (scheduleRef.value?.resetToDefault) scheduleRef.value.resetToDefault();
  resetIdleTimer();
};"""
content = content.replace(old_timeout, new_timeout)

with open('/Users/admin/Desktop/робота/Kiosk/src/App.vue', 'w') as f:
    f.write(content)

print("App.vue updated")
