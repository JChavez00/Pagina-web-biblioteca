document.addEventListener('DOMContentLoaded', () => {
    // Header Scroll Effect
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
            navbar.style.padding = '0';
        } else {
            navbar.style.boxShadow = 'var(--shadow-sm)';
        }
    });

    // Mobile Menu Toggle (Basic implementation)
    const menuToggle = document.getElementById('mobile-menu');
    const navLinks = document.querySelector('.nav-links');
    
    // Simple toggle logic
    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            if (navLinks.style.display === 'flex') {
                navLinks.style.display = 'none';
            } else {
                navLinks.style.display = 'flex';
                navLinks.style.flexDirection = 'column';
                navLinks.style.position = 'absolute';
                navLinks.style.top = '80px';
                navLinks.style.left = '0';
                navLinks.style.width = '100%';
                navLinks.style.backgroundColor = 'white';
                navLinks.style.padding = '1rem';
                navLinks.style.boxShadow = 'var(--shadow-md)';
            }
        });
    }

    // Search Tabs interaction
    const searchTabs = document.querySelectorAll('.search-tabs button');
    
    searchTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove active class from all tabs
            searchTabs.forEach(t => t.classList.remove('active'));
            // Add active class to clicked tab
            tab.classList.add('active');
            
            // Optional: change input placeholder based on selection
            const input = document.querySelector('.search-input-container input');
            const placeholderText = `Buscar en ${tab.textContent.toLowerCase()}...`;
            if (tab.textContent === "Todo") {
                input.placeholder = "Buscar libros, artÃ­culos, tesis y mÃ¡s...";
            } else {
                input.placeholder = placeholderText;
            }
        });
    });
});


// Inicializar Swiper (Carrusel)
document.addEventListener('DOMContentLoaded', () => {
    if (typeof Swiper !== 'undefined') {
        const swiper = new Swiper('.mySwiper', {
            slidesPerView: 1,
            spaceBetween: 20,
            loop: true,
            autoplay: {
                delay: 3000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            breakpoints: {
                640: { slidesPerView: 2, spaceBetween: 20 },
                768: { slidesPerView: 3, spaceBetween: 30 },
                1024: { slidesPerView: 4, spaceBetween: 30 }
            }
        });
    }
});

// --- Búsqueda Inteligente (Dropdown) ---
document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.querySelector('.search-input-container input');
    
    if (searchInput) {
        // Crear el contenedor de sugerencias
        const dropdown = document.createElement('div');
        dropdown.className = 'search-dropdown';
        dropdown.innerHTML = 
            <ul>
                <li><i class="fas fa-search"></i> <span>Cálculo de una variable</span></li>
                <li><i class="fas fa-search"></i> <span>Física Universitaria</span></li>
                <li><i class="fas fa-search"></i> <span>Metodología de la investigación</span></li>
                <li><i class="fas fa-book"></i> <span>Ver todos los resultados para "<strong class="search-term"></strong>"</span></li>
            </ul>
        ;
        
        searchInput.parentElement.appendChild(dropdown);
        
        const searchTermSpan = dropdown.querySelector('.search-term');

        searchInput.addEventListener('input', (e) => {
            const val = e.target.value.trim();
            if (val.length > 0) {
                searchTermSpan.textContent = val;
                dropdown.classList.add('active');
            } else {
                dropdown.classList.remove('active');
            }
        });

        // Ocultar al hacer clic fuera
        document.addEventListener('click', (e) => {
            if (!searchInput.contains(e.target) && !dropdown.contains(e.target)) {
                dropdown.classList.remove('active');
            }
        });
    }
});

// --- Filtrado en Vivo (Catálogo) ---
document.addEventListener('DOMContentLoaded', () => {
    const checkboxes = document.querySelectorAll('.filter-box input[type="checkbox"]');
    const bookCards = document.querySelectorAll('.catalog-main .book-card');

    if (checkboxes.length > 0 && bookCards.length > 0) {
        checkboxes.forEach(checkbox => {
            checkbox.addEventListener('change', () => {
                // Simulación visual simple: desvanece un par de tarjetas al azar para mostrar el efecto
                bookCards.forEach(card => {
                    if (Math.random() > 0.5) {
                        card.style.opacity = '0';
                        setTimeout(() => card.style.display = 'none', 300);
                    } else {
                        card.style.display = 'block';
                        setTimeout(() => card.style.opacity = '1', 50);
                    }
                });
            });
        });
    }
});

   // --- Navbar Background on Scroll ---
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }
