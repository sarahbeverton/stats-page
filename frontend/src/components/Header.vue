
<template>
    <header class="rvt-header-wrapper">
        <!-- Hidden link for keyboard users to skip to main content -->
        <a class="rvt-header-wrapper__skip-link" href="#main-content">Skip to main content</a>
        <div class="rvt-header-global">
            <div class="rvt-container-xl">
                <div class="rvt-header-global__inner">
                <div class="rvt-header-global__logo-slot">
                    <a class="rvt-lockup" href="/">
                    <!-- Trident logo -->
                    <div class="rvt-lockup__tab">
                        <svg xmlns="http://www.w3.org/2000/svg" class="rvt-lockup__trident" viewBox="0 0 28 34">
                        <path d="M-3.34344e-05 4.70897H8.83308V7.174H7.1897V21.1426H10.6134V2.72321H8.83308V0.121224H18.214V2.65476H16.2283V21.1426H19.7889V7.174H18.214V4.64047H27.0471V7.174H25.0614V23.6761L21.7746 26.8944H16.2967V30.455H18.214V33.8787H8.76463V30.592H10.6819V26.8259H5.20403L1.91726 23.6077V7.174H-3.34344e-05V4.70897Z" fill="currentColor"></path>
                        </svg>
                    </div>
                    <!-- Website or application title -->
                    <div class="rvt-lockup__body">
                        <span class="rvt-lockup__title">OSoMe Data and Tool Stats</span>
                        <span class="rvt-lockup__subtitle">Indiana University Bloomington</span>
                    </div>
                    </a>
                </div>

                <!--Header controls-->
                <!-- <div class="rvt-header-global__controls">
                   
                    <div data-rvt-disclosure="search" data-rvt-close-click-outside>
                  
                    <button class="rvt-global-toggle" data-rvt-disclosure-toggle="search" aria-expanded="false">
                        <span class="rvt-sr-only">Search</span>
                        <svg class="rvt-global-toggle__search" fill="currentColor" width="16" height="16" viewBox="0 0 16 16"><path d="M7 2a5 5 0 1 0 0 10A5 5 0 0 0 7 2ZM0 7a7 7 0 1 1 12.606 4.192l3.101 3.1-1.414 1.415-3.1-3.1A7 7 0 0 1 0 7Z"></path></svg>
                    </button>
                   
                    <form action="/search" class="rvt-header-global__search" data-rvt-disclosure-target="search" role="search" method="get" hidden>
                        <label class="rvt-sr-only" for="search">Search</label>
                        <div class="rvt-input-group">
                        <input id="search" class="rvt-input-group__input rvt-text-input" type="text" name="q">
                        <div class="rvt-input-group__append">
                            <button class="rvt-button">Search</button>
                        </div>
                        </div>
                    </form>
                    </div>
                </div> -->
            </div>
        </div>
        </div>
    </header>
</template>

<script lang="ts" setup>
</script>