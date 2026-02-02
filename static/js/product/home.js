// // --- Dummy Data ---
// const products = [
//     { id: 1, name: "Noise-Canceling Headphones", price: 299.99, rating: 4.8, image: "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" },
//     { id: 2, name: "Mechanical Keyboard", price: 129.50, rating: 4.7, image: "https://images.unsplash.com/photo-1587829741301-dc798b91a603?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" },
//     { id: 3, name: "Ergonomic Office Chair", price: 349.00, rating: 4.5, image: "https://images.unsplash.com/photo-1580480055273-228ff5388ef8?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" },
//     { id: 4, name: "Smart Watch Series 5", price: 199.99, rating: 4.6, image: "https://images.unsplash.com/photo-1523275335684-37898b6baf30?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" },
//     { id: 5, name: "Minimalist Desk Lamp", price: 49.95, rating: 4.2, image: "https://images.unsplash.com/photo-1507473888900-52e1ad14592a?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" },
//     { id: 6, name: "Premium Coffee Maker", price: 89.99, rating: 4.9, image: "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80" }
// ];

// // --- Selectors ---
// const productGrid = document.getElementById('product-grid');
// const searchInput = document.getElementById('search-input');
// const noResults = document.getElementById('no-results');

// // --- Functions ---
// function getStars(rating) {
//     const fullStars = Math.floor(rating);
//     const hasHalf = rating % 1 !== 0;
//     let starsHtml = '';
//     for(let i=0; i<fullStars; i++) starsHtml += '★';
//     if(hasHalf) starsHtml += '½';
//     return starsHtml;
// }

// // function renderProducts(data) {
// //     productGrid.innerHTML = '';
// //     if (data.length === 0) {
// //         noResults.classList.remove('hidden');
// //         return;
// //     } else {
// //         noResults.classList.add('hidden');
// //     }

// //     data.forEach(product => {
// //         const card = document.createElement('div');
// //         card.classList.add('product-card');
// //         card.innerHTML = `
// //             <div class="card-img-container">
// //                 <img src="${product.image}" alt="${product.name}" class="card-img">
// //             </div>
// //             <div class="card-body">
// //                 <h3 class="product-title">${product.name}</h3>
// //                 <div class="product-rating">${getStars(product.rating)} (${product.rating})</div>
// //                 <div class="card-footer">
// //                     <span class="price">$${product.price.toFixed(2)}</span>
// //                     <button class="add-btn" onclick="alert('Added to cart!')">Add</button>
// //                 </div>
// //             </div>
// //         `;
// //         productGrid.appendChild(card);
// //     });
// // }

// function handleSearch(e) {
//     const searchTerm = e.target.value.toLowerCase().trim();
//     const filteredProducts = products.filter(product => 
//         product.name.toLowerCase().includes(searchTerm)
//     );
//     renderProducts(filteredProducts);
// }

// // --- Event Listeners ---
// document.addEventListener('DOMContentLoaded', () => {
//     renderProducts(products);
// });

// searchInput.addEventListener('input', handleSearch);

// // Add Active State Logic for Bottom Nav
// // const navItems = document.querySelectorAll('.bottom-nav-item');
// // navItems.forEach(item => {
// //     item.addEventListener('click', (e) => {
// //         // Prevent default anchor jump for demo
// //         e.preventDefault();
        
// //         // Remove active class from all
// //         navItems.forEach(nav => nav.classList.remove('active'));
        
// //         // Add active to clicked (handle bubble up if icon clicked)
// //         const target = e.target.closest('.bottom-nav-item');
// //         target.classList.add('active');
// //     });
// // });