<script>
  import '../../../app.css';
  import { enhance } from '$app/forms';

  import imgGoogle from '$lib/assets/images/google.svg';
  import imgLogo from '$lib/assets/images/logo.png';
  import { ArrowRight } from '@lucide/svelte';

  let { data = {} } = $props();

  let isLoading = $state(false);
  let email = $state('');
  let magicLinkSent = $state(false);
  let isSendingLink = $state(false);
  let magicLinkError = $state('');

  function handleGoogleLogin() {
    isLoading = true;
  }

  function handleMagicLink() {
    isSendingLink = true;
    magicLinkError = '';
    return async ({ result }) => {
      isSendingLink = false;
      if (result?.type === 'success') {
        magicLinkSent = true;
      } else if (result?.type === 'failure') {
        magicLinkError = result.data?.error || 'Something went wrong. Please try again.';
      } else if (!result) {
        magicLinkError = 'Something went wrong. Please try again.';
      }
    };
  }
</script>

<svelte:head>
  <title>Sign in | BottleCRM</title>
  <meta
    name="description"
    content="Sign in or sign up for BottleCRM to manage your contacts, deals, and grow your business."
  />
</svelte:head>

<div class="login-page">
  <!-- Main Container -->
  <div class="login-wrapper">
    <!-- Logo -->
    <a href="/" class="logo">
      <img src={imgLogo} alt="" class="logo-icon" />
      <span class="logo-text">Marryo<span class="logo-text-crm"> CRM</span></span>
    </a>

    <!-- Login Card -->
    <div class="login-card">
      <h1 class="login-title">Welcome back</h1>
      <p class="login-subtitle">Sign in to your MarryoCRM account</p>

      <!-- Google Sign In -->
      <a
        href={data['google_url']}
        onclick={handleGoogleLogin}
        class="google-btn"
        class:loading={isLoading}
      >
        {#if isLoading}
          <span class="spinner"></span>
          <span>Redirecting...</span>
        {:else}
          <img src={imgGoogle} alt="" class="google-icon" />
          <span>Continue with Google</span>
        {/if}
      </a>

      <!-- Divider -->
      <div class="divider">
        <span>or</span>
      </div>

      <!-- Magic Link -->
      {#if magicLinkSent}
        <div class="magic-link-success">
          <p>Check your email for a sign-in link.</p>
          <p class="magic-link-hint">The link expires in 10 minutes.</p>
        </div>
      {:else}
        <form method="POST" use:enhance={handleMagicLink} class="magic-link-form">
          <input
            type="email"
            name="email"
            placeholder="Enter your email address"
            class="email-input"
            required
            bind:value={email}
            disabled={isSendingLink}
          />
          <button type="submit" class="magic-link-btn" disabled={isSendingLink}>
            {#if isSendingLink}
              <span class="spinner"></span>
              <span>Sending...</span>
            {:else}
              <span>Continue with email</span>
              <ArrowRight size={16} />
            {/if}
          </button>
        </form>
        {#if magicLinkError}
          <p class="magic-link-error">{magicLinkError}</p>
        {/if}
      {/if}
    </div>

    <!-- Help Links -->
    <div class="help-section">
      <p class="help-text">New here? Just enter your email above to get started.</p>
    </div>

    <!-- Footer -->
    <footer class="login-footer">
      <a href="https://bottlecrm.io/privacy-policy">Privacy Policy</a>
      <span class="dot"></span>
      <a href="https://bottlecrm.io/terms">Terms of Service</a>
      <span class="dot"></span>
      <a href="https://github.com/MicroPyramid/Django-CRM" target="_blank" rel="noopener">GitHub</a>
    </footer>
  </div>
</div>

<style>
  .login-page {
    min-height: 100vh;
    min-height: 100dvh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: hsl(45, 33%, 97%);
    background-image:
      radial-gradient(ellipse at 15% 20%, hsl(350, 45%, 92%) 0px, transparent 55%),
      radial-gradient(ellipse at 85% 80%, hsl(38, 50%, 88%) 0px, transparent 55%),
      radial-gradient(ellipse at 50% 50%, hsl(45, 40%, 96%) 0px, transparent 70%);
    padding: 2rem;
  }

  .login-wrapper {
    width: 100%;
    max-width: 420px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  /* Logo */
  .logo {
    display: flex;
    align-items: center;
    gap: 0.625rem;
    text-decoration: none;
    margin-bottom: 2.25rem;
  }

  .logo-icon {
    width: 40px;
    height: 40px;
    object-fit: contain;
  }

  .logo-text {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.75rem;
    font-weight: 700;
    color: hsl(350, 45%, 30%);
    letter-spacing: 0.04em;
  }

  .logo-text-crm {
    font-family: 'Inter', sans-serif;
    font-size: 1rem;
    font-weight: 500;
    color: hsl(38, 50%, 55%);
    letter-spacing: 0.02em;
    vertical-align: middle;
  }

  /* Login Card */
  .login-card {
    width: 100%;
    background: hsl(45, 40%, 99%);
    border-radius: 16px;
    padding: 2.5rem 2.25rem;
    box-shadow:
      0 2px 12px rgba(80, 20, 10, 0.06),
      0 8px 32px rgba(80, 20, 10, 0.08);
    border: 1px solid hsl(38, 25%, 88%);
  }

  .login-title {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.875rem;
    font-weight: 600;
    color: hsl(350, 45%, 30%);
    text-align: center;
    margin: 0 0 0.375rem;
    letter-spacing: 0.02em;
    line-height: 1.2;
  }

  .login-subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 0.875rem;
    color: hsl(20, 8%, 52%);
    text-align: center;
    margin: 0 0 1.75rem;
    letter-spacing: -0.01em;
  }

  /* Google Button */
  .google-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
    width: 100%;
    height: 48px;
    background: hsl(350, 45%, 30%);
    border: none;
    border-radius: 8px;
    color: hsl(45, 33%, 97%);
    font-family: 'Inter', sans-serif;
    font-size: 0.9375rem;
    font-weight: 600;
    text-decoration: none;
    cursor: pointer;
    transition: background-color 0.15s ease, transform 0.1s ease, box-shadow 0.15s ease;
    letter-spacing: -0.01em;
  }

  .google-btn:hover {
    background: hsl(350, 45%, 24%);
    box-shadow: 0 4px 12px rgba(80, 20, 10, 0.2);
  }

  .google-btn:active {
    background: hsl(350, 45%, 20%);
    transform: scale(0.99);
  }

  .google-btn.loading {
    pointer-events: none;
    opacity: 0.85;
  }

  .google-icon {
    width: 20px;
    height: 20px;
    background: hsl(45, 40%, 99%);
    border-radius: 4px;
    padding: 2px;
  }

  .spinner {
    width: 18px;
    height: 18px;
    border: 2px solid rgba(255, 245, 230, 0.35);
    border-top-color: hsl(45, 33%, 97%);
    border-radius: 50%;
    animation: spin 0.7s linear infinite;
  }

  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }

  /* Divider */
  .divider {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin: 1.5rem 0;
  }

  .divider::before,
  .divider::after {
    content: '';
    flex: 1;
    height: 1px;
    background: hsl(38, 25%, 88%);
  }

  .divider span {
    font-family: 'Inter', sans-serif;
    font-size: 0.75rem;
    color: hsl(20, 6%, 58%);
    text-transform: lowercase;
    letter-spacing: 0.05em;
  }

  /* Magic Link Form */
  .magic-link-form {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .email-input {
    width: 100%;
    height: 48px;
    padding: 0 1rem;
    border: 1.5px solid hsl(38, 25%, 88%);
    border-radius: 8px;
    font-family: 'Inter', sans-serif;
    font-size: 0.9375rem;
    color: hsl(20, 15%, 15%);
    background: hsl(45, 40%, 99%);
    outline: none;
    transition: border-color 0.15s ease, box-shadow 0.15s ease;
    box-sizing: border-box;
  }

  .email-input::placeholder {
    color: hsl(20, 6%, 62%);
  }

  .email-input:focus {
    border-color: hsl(350, 45%, 30%);
    box-shadow: 0 0 0 3px hsl(350, 45%, 96%);
  }

  .email-input:disabled {
    opacity: 0.6;
  }

  .magic-link-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    width: 100%;
    height: 48px;
    background: hsl(38, 50%, 55%);
    border: none;
    border-radius: 8px;
    color: hsl(45, 33%, 97%);
    font-family: 'Inter', sans-serif;
    font-size: 0.9375rem;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.15s ease, transform 0.1s ease, box-shadow 0.15s ease;
    letter-spacing: -0.01em;
  }

  .magic-link-btn:hover {
    background: hsl(38, 55%, 45%);
    box-shadow: 0 4px 12px rgba(120, 85, 25, 0.22);
  }

  .magic-link-btn:active {
    transform: scale(0.99);
  }

  .magic-link-btn:disabled {
    opacity: 0.85;
    pointer-events: none;
  }

  .magic-link-success {
    text-align: center;
    padding: 1rem 0;
  }

  .magic-link-error {
    margin-top: 0.75rem;
    font-size: 0.875rem;
    color: hsl(0, 65%, 40%);
    text-align: center;
  }

  .magic-link-success p {
    color: hsl(350, 45%, 30%);
    font-size: 1rem;
    font-weight: 500;
    margin: 0;
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.25rem;
  }

  .magic-link-hint {
    color: hsl(20, 8%, 52%) !important;
    font-size: 0.875rem !important;
    font-weight: 400 !important;
    font-family: 'Inter', sans-serif !important;
    margin-top: 0.5rem !important;
  }

  /* Help Section */
  .help-section {
    margin-top: 1.5rem;
    text-align: center;
  }

  .help-text {
    font-family: 'Inter', sans-serif;
    font-size: 0.875rem;
    color: hsl(20, 8%, 52%);
    margin: 0;
  }

  /* Footer */
  .login-footer {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
    margin-top: 2rem;
    flex-wrap: wrap;
  }

  .login-footer a {
    font-family: 'Inter', sans-serif;
    font-size: 0.8125rem;
    color: hsl(20, 6%, 52%);
    text-decoration: none;
    transition: color 0.15s ease;
  }

  .login-footer a:hover {
    color: hsl(350, 45%, 30%);
  }

  .dot {
    width: 3px;
    height: 3px;
    border-radius: 50%;
    background: hsl(38, 25%, 80%);
  }

  /* Responsive */
  @media (max-width: 480px) {
    .login-page {
      padding: 1.5rem;
      align-items: flex-start;
      padding-top: 3rem;
    }

    .login-card {
      padding: 2rem 1.5rem;
    }

    .login-title {
      font-size: 1.625rem;
    }
  }

  /* Dark mode support */
  :global(.dark) .login-page {
    background: hsl(20, 12%, 10%);
    background-image:
      radial-gradient(ellipse at 15% 20%, rgba(155, 40, 60, 0.18) 0px, transparent 55%),
      radial-gradient(ellipse at 85% 80%, rgba(140, 100, 40, 0.15) 0px, transparent 55%);
  }

  :global(.dark) .login-card {
    background: hsl(20, 10%, 14%);
    border-color: hsl(20, 10%, 22%);
    box-shadow:
      0 2px 12px rgba(0, 0, 0, 0.25),
      0 8px 32px rgba(0, 0, 0, 0.3);
  }

  :global(.dark) .logo-text {
    color: hsl(350, 50%, 62%);
  }

  :global(.dark) .login-title {
    color: hsl(350, 50%, 62%);
  }

  :global(.dark) .login-subtitle {
    color: hsl(30, 8%, 55%);
  }

  :global(.dark) .divider::before,
  :global(.dark) .divider::after {
    background: hsl(20, 10%, 28%);
  }

  :global(.dark) .divider span {
    color: hsl(20, 6%, 45%);
  }

  :global(.dark) .email-input {
    background: hsl(20, 10%, 16%);
    border-color: hsl(20, 10%, 26%);
    color: hsl(45, 20%, 90%);
  }

  :global(.dark) .email-input::placeholder {
    color: hsl(20, 6%, 42%);
  }

  :global(.dark) .email-input:focus {
    border-color: hsl(350, 50%, 55%);
    box-shadow: 0 0 0 3px rgba(155, 40, 60, 0.15);
  }

  :global(.dark) .magic-link-btn {
    background: hsl(38, 50%, 48%);
    color: hsl(45, 33%, 97%);
  }

  :global(.dark) .magic-link-btn:hover {
    background: hsl(38, 55%, 55%);
  }

  :global(.dark) .magic-link-success p {
    color: hsl(45, 20%, 88%);
  }

  :global(.dark) .help-text {
    color: hsl(20, 6%, 48%);
  }

  :global(.dark) .login-footer a {
    color: hsl(20, 6%, 42%);
  }

  :global(.dark) .login-footer a:hover {
    color: hsl(350, 50%, 62%);
  }

  :global(.dark) .dot {
    background: hsl(20, 8%, 30%);
  }
</style>
