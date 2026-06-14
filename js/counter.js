/* ============================================================
   CANVAS KOLKATA — Counter Animation
   Animated number counters that trigger when scrolled into view
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  /**
   * Animate a number from 0 to its target value
   * @param {HTMLElement} element - The DOM element containing the number
   * @param {number} target - The target number
   * @param {number} duration - Animation duration in ms
   * @param {string} suffix - Suffix to append (e.g., '+', '%', 'K')
   */
  const animateCounter = (element, target, duration = 2000, suffix = '') => {
    let startTime = null;
    const startValue = 0;

    const easeOutQuad = (t) => t * (2 - t);

    const step = (timestamp) => {
      if (!startTime) startTime = timestamp;
      const elapsed = timestamp - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const easedProgress = easeOutQuad(progress);
      const currentValue = Math.floor(startValue + (target - startValue) * easedProgress);

      element.textContent = currentValue.toLocaleString('en-IN') + suffix;

      if (progress < 1) {
        requestAnimationFrame(step);
      } else {
        element.textContent = target.toLocaleString('en-IN') + suffix;
      }
    };

    requestAnimationFrame(step);
  };

  // Find all counter elements
  const counters = document.querySelectorAll('[data-counter]');

  if (counters.length > 0) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseInt(el.getAttribute('data-counter'), 10);
          const suffix = el.getAttribute('data-suffix') || '';
          const duration = parseInt(el.getAttribute('data-duration'), 10) || 2000;

          animateCounter(el, target, duration, suffix);
          counterObserver.unobserve(el);
        }
      });
    }, {
      threshold: 0.3
    });

    counters.forEach(counter => counterObserver.observe(counter));
  }
});
