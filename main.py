import pyautogui
import time
from random import randint

interval = 0.2
time.sleep(20)

text_script = "getReportsData$ = this.onGetReportsData$.pipe(\n switchMap((response: IReportPagination) => {\n this.fetching = true;\n this.currentPage = this.isFilter ? 1 : this.currentPage;\n const tempData = response.filteredForm;\n tempData.orderBy = 'publishDate';\n\n return this.reports.getReportsData(response, this.pageSize, this.currentPage, tempData).pipe(\n finalize(() => {\n this.isFilter = false;\n })\n );\n }),\n tap((data) => {\n if (data?.items) {\n const { items, pageNumber, totalCount } = data;\n this.items = items;\n this.pageNumber = pageNumber;\n this.totalItems = totalCount;\n }\n }),\n debounceTime(1000),\n tap(() => {\n this.fetching = false;\n })\n );"
text_html = '<div class="container">\n <header class="header">\n <nav class="navbar">\n <ul class="nav-list">\n <li class="nav-item"><a href="#" class="nav-link">Home</a></li>\n <li class="nav-item"><a href="#" class="nav-link">About</a></li>\n <li class="nav-item"><a href="#" class="nav-link">Services</a></li>\n <li class="nav-item"><a href="#" class="nav-link">Contact</a></li>\n </ul>\n </nav>\n <div class="search-bar">\n <input type="text" class="search-input" placeholder="Search...">\n <button class="search-button">Search</button>\n </div>\n </header>\n\n <main class="main-content">\n <section class="hero">\n <div class="hero-content">\n <h1 class="hero-title">Welcome to Our Website</h1>\n <p class="hero-subtitle">We provide amazing services for you.</p>\n <button class="hero-button">Get Started</button>\n </div>\n </section>\n\n <section class="features">\n <div class="feature-item">\n <h2 class="feature-title">Feature One</h2>\n <p class="feature-description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum.</p>\n </div>\n <div class="feature-item">\n <h2 class="feature-title">Feature Two</h2>\n <p class="feature-description">Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus.</p>\n </div>\n <div class="feature-item">\n <h2 class="feature-title">Feature Three</h2>\n <p class="feature-description">Quisque velit nisi, pretium ut lacinia in, elementum id enim.</p>\n </div>\n </section>\n\n <section class="testimonials">\n <h2 class="section-title">What Our Clients Say</h2>\n <div class="testimonial-item">\n <p class="testimonial-text">"This service is amazing! Highly recommended."</p>\n <p class="testimonial-author">- John Doe</p>\n </div>\n <div class="testimonial-item">\n <p class="testimonial-text">"Excellent customer service and great results."</p>\n <p class="testimonial-author">- Jane Smith</p>\n </div>\n </section>\n </main>\n\n <footer class="footer">\n <div class="footer-content">\n <p class="footer-text">© 2024 Your Company. All rights reserved.</p>\n <ul class="social-links">\n <li><a href="#" class="social-link">Facebook</a></li>\n <li><a href="#" class="social-link">Twitter</a></li>\n <li><a href="#" class="social-link">Instagram</a></li>\n </ul>\n </div>\n </footer>\n</div>'

positions = [
    (391, 51,'html'),
    (799, 354,'center'),
    (726, 47,'html'),
    (708, 337,'center'),
    (543, 53,'html'),
    (664, 412,'center'),
    (872, 47,'html'),
    (622, 339,'center'),
]

def move_click_and_write(x, y, text_type, rand):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.scroll(10*rand)
    if text_type == 'html':
        pyautogui.write(text_html, interval=interval)
    elif text_type == 'script':
        pyautogui.write(text_script, interval=interval)
    time.sleep(rand)

try:
    while True:
        rand = randint(1, 5)
        for position in positions:
            move_click_and_write(position[0], position[1], position[2], rand)
        
except KeyboardInterrupt:
    print("Done")