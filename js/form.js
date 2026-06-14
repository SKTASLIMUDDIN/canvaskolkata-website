/* ============================================================
   CANVAS KOLKATA — Form Handling & WhatsApp Integration
   Contact form validation & WhatsApp redirect
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  const WHATSAPP_NUMBER = '919007738004';
  const WHATSAPP_BASE_URL = `https://wa.me/${WHATSAPP_NUMBER}`;

  // ===== CONTACT FORM =====
  const contactForm = document.getElementById('contact-form');

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      // Clear previous errors
      contactForm.querySelectorAll('.form-group').forEach(group => {
        group.classList.remove('error');
      });

      // Get form values
      const name = contactForm.querySelector('#contact-name');
      const email = contactForm.querySelector('#contact-email');
      const phone = contactForm.querySelector('#contact-phone');
      const service = contactForm.querySelector('#contact-service');
      const message = contactForm.querySelector('#contact-message');

      let isValid = true;

      // Validate name
      if (!name || name.value.trim().length < 2) {
        showError(name, 'Please enter your full name');
        isValid = false;
      }

      // Validate email
      if (!email || !isValidEmail(email.value)) {
        showError(email, 'Please enter a valid email address');
        isValid = false;
      }

      // Validate phone
      if (!phone || phone.value.trim().length < 10) {
        showError(phone, 'Please enter a valid phone number');
        isValid = false;
      }

      // Validate service
      if (!service || !service.value) {
        showError(service, 'Please select a service');
        isValid = false;
      }

      // Validate message
      if (!message || message.value.trim().length < 10) {
        showError(message, 'Please enter your message (minimum 10 characters)');
        isValid = false;
      }

      if (isValid) {
        // Build WhatsApp message
        const whatsappMessage = encodeURIComponent(
          `🎨 *New Inquiry from Canvas Kolkata Website*\n\n` +
          `👤 *Name:* ${name.value.trim()}\n` +
          `📧 *Email:* ${email.value.trim()}\n` +
          `📱 *Phone:* ${phone.value.trim()}\n` +
          `🛠️ *Service:* ${service.options[service.selectedIndex].text}\n` +
          `💬 *Message:* ${message.value.trim()}\n\n` +
          `---\n` +
          `Sent from canvaskolkata.com`
        );

        // Show success state
        const formInner = contactForm.querySelector('.form-inner');
        const formSuccess = contactForm.querySelector('.form-success');

        if (formInner && formSuccess) {
          formInner.style.display = 'none';
          formSuccess.classList.add('show');
        }

        // Open WhatsApp
        setTimeout(() => {
          window.open(`${WHATSAPP_BASE_URL}?text=${whatsappMessage}`, '_blank');
        }, 800);

        // Reset form after delay
        setTimeout(() => {
          contactForm.reset();
          if (formInner && formSuccess) {
            formInner.style.display = '';
            formSuccess.classList.remove('show');
          }
        }, 5000);
      }
    });
  }

  // ===== QUOTE FORM (Quick Quote in Services/Pricing) =====
  const quoteButtons = document.querySelectorAll('[data-quote]');

  quoteButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const service = btn.getAttribute('data-quote') || 'General Inquiry';

      const whatsappMessage = encodeURIComponent(
        `Hi Canvas Kolkata! 👋\n\n` +
        `I'm interested in your *${service}* service.\n` +
        `Could you please share more details and pricing?\n\n` +
        `Thank you!`
      );

      window.open(`${WHATSAPP_BASE_URL}?text=${whatsappMessage}`, '_blank');
    });
  });

  // ===== NEWSLETTER FORM =====
  const newsletterForm = document.getElementById('newsletter-form');

  if (newsletterForm) {
    newsletterForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const emailInput = newsletterForm.querySelector('input[type="email"]');

      if (emailInput && isValidEmail(emailInput.value)) {
        const whatsappMessage = encodeURIComponent(
          `Hi Canvas Kolkata! 📬\n\n` +
          `I'd like to subscribe to your newsletter.\n` +
          `My email: ${emailInput.value.trim()}\n\n` +
          `Thank you!`
        );

        window.open(`${WHATSAPP_BASE_URL}?text=${whatsappMessage}`, '_blank');
        emailInput.value = '';

        // Show brief success feedback
        const btn = newsletterForm.querySelector('button');
        if (btn) {
          const originalHTML = btn.innerHTML;
          btn.innerHTML = '<i class="fas fa-check"></i>';
          btn.style.background = '#00D4AA';
          setTimeout(() => {
            btn.innerHTML = originalHTML;
            btn.style.background = '';
          }, 2000);
        }
      }
    });
  }

  // ===== HELPER FUNCTIONS =====

  /**
   * Show error on a form field
   */
  function showError(field, message) {
    if (!field) return;
    const group = field.closest('.form-group');
    if (group) {
      group.classList.add('error');
      const errorEl = group.querySelector('.form-error');
      if (errorEl) {
        errorEl.textContent = message;
      }
    }
  }

  /**
   * Validate email format
   */
  function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  }

  // ===== REAL-TIME FIELD VALIDATION =====
  const formInputs = document.querySelectorAll('.form-group input, .form-group textarea, .form-group select');

  formInputs.forEach(input => {
    input.addEventListener('input', () => {
      const group = input.closest('.form-group');
      if (group && group.classList.contains('error')) {
        group.classList.remove('error');
      }
    });
  });
});
