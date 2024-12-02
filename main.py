import sys
try:
    from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QCalendarWidget, QPushButton, QLabel,
                               QStackedWidget, QTimeEdit, QFrame)
    from PyQt6.QtCore import QTimer, QDateTime, Qt, QTime, QPropertyAnimation, QEasingCurve, QPoint, QPointF
    from PyQt6.QtGui import QFont, QColor, QLinearGradient, QPalette, QIcon
except ImportError:
    print("Error: PyQt6 is not installed. Please install it using: pip install PyQt6")
    sys.exit(1)

import datetime
import random

class ModernFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("modernFrame")
        self.setStyleSheet("""
            #modernFrame {
                background-color: rgba(32, 32, 32, 0.95);
                border-radius: 15px;
                border: 1px solid rgba(255, 255, 255, 0.1);
                padding: 20px;
                margin: 10px;
            }
        """)

class ModernButton(QPushButton):
    def __init__(self, text, color="#4299E1"):
        super().__init__(text)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: 2px solid {color};
                padding: 12px 25px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {self.adjust_color(color, -20)};
                border-color: {self.adjust_color(color, -20)};
            }}
            QPushButton:pressed {{
                background-color: {self.adjust_color(color, -40)};
                border-color: {self.adjust_color(color, -40)};
            }}
        """)

    def adjust_color(self, hex_color, factor):
        # Darken or lighten color
        c = QColor(hex_color)
        h, s, v, a = c.getHsv()
        v = max(0, min(255, v + factor))
        c.setHsv(h, s, v, a)
        return c.name()

class AgeCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern Age Calculator")
        self.setMinimumSize(900, 700)
        
        # Set up main widget with gradient background
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # Create gradient background
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #4158D0,
                    stop: 0.46 #C850C0,
                    stop: 1 #FFCC70
                );
            }
        """)
        
        # Create stacked widget for multiple pages
        self.stacked_widget = QStackedWidget()
        layout = QVBoxLayout(main_widget)
        layout.addWidget(self.stacked_widget)
        
        # Create pages
        self.create_welcome_page()
        self.create_date_picker_page()
        self.create_result_page()
        
        # Timer for real-time updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_age)
        self.timer.start(1000)

    def create_welcome_page(self):
        welcome_widget = QWidget()
        layout = QVBoxLayout(welcome_widget)
        layout.setSpacing(30)
        
        # Create glass-morphism container
        container = ModernFrame()
        container_layout = QVBoxLayout(container)
        
        # Welcome message
        welcome_label = QLabel("✨ Age Calculator")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setFont(QFont('Segoe UI', 32, QFont.Weight.Bold))
        welcome_label.setStyleSheet("color: white;")
        
        # Description
        desc_label = QLabel("Discover your journey through time")
        desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        desc_label.setFont(QFont('Segoe UI', 16))
        desc_label.setStyleSheet("color: #E2E8F0; margin-bottom: 20px;")
        
        # Start button
        start_btn = ModernButton("Begin Journey", "#8B5CF6")
        start_btn.setFixedSize(200, 50)
        start_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        
        # Page indicator
        page_indicator = QLabel("1/3")
        page_indicator.setAlignment(Qt.AlignmentFlag.AlignCenter)
        page_indicator.setStyleSheet("""
            color: #718096;
            font-size: 14px;
            font-weight: bold;
            background: rgba(255, 255, 255, 0.2);
            padding: 5px 15px;
            border-radius: 15px;
        """)
        
        container_layout.addStretch()
        container_layout.addWidget(welcome_label)
        container_layout.addWidget(desc_label)
        container_layout.addWidget(start_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        container_layout.addStretch()
        container_layout.addWidget(page_indicator)
        
        layout.addStretch()
        layout.addWidget(container)
        layout.addStretch()
        
        self.stacked_widget.addWidget(welcome_widget)

    def create_date_picker_page(self):
        picker_widget = QWidget()
        layout = QVBoxLayout(picker_widget)
        layout.setSpacing(20)
        
        # Create glass-morphism container
        container = ModernFrame()
        container_layout = QVBoxLayout(container)
        
        # Title
        title = QLabel("Select Your Birth Date & Time")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont('Segoe UI', 24, QFont.Weight.Bold))
        title.setStyleSheet("color: white; margin-bottom: 20px;")
        
        # Calendar with modern styling
        self.calendar = QCalendarWidget()
        self.calendar.setFixedHeight(350)
        self.calendar.setStyleSheet("""
            QCalendarWidget {
                background-color: transparent;
            }
            QCalendarWidget QToolButton {
                color: white;
                background-color: transparent;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 14px;
                min-width: 80px;
            }
            QCalendarWidget QToolButton:hover {
                background-color: rgba(255, 255, 255, 0.1);
            }
            QCalendarWidget QMenu {
                background-color: #202020;
                border: 1px solid #404040;
                border-radius: 5px;
                color: white;
                padding: 4px;
            }
            QCalendarWidget QSpinBox {
                background-color: #202020;
                color: white;
                border-radius: 5px;
                padding: 5px;
                selection-background-color: #0078D4;
            }
            /* Calendar table styling */
            QCalendarWidget QTableView {
                background-color: rgba(32, 32, 32, 0.95);
                selection-background-color: #0078D4;
                selection-color: white;
                color: white;
                border-radius: 8px;
                padding: 5px;
                font-size: 13px;
            }
            /* Header row styling */
            QCalendarWidget QTableView QHeaderView {
                background-color: transparent;
            }
            QCalendarWidget QTableView QHeaderView::section {
                color: #99A3A4;
                padding: 6px;
                font-size: 13px;
            }
            /* Individual day numbers */
            QCalendarWidget QTableView QTableCornerButton::section {
                background-color: transparent;
                border: none;
            }
            QCalendarWidget QAbstractItemView:enabled {
                color: white;
                selection-background-color: #0078D4;
                selection-color: white;
                font-size: 13px;
            }
            QCalendarWidget QAbstractItemView:disabled {
                color: #666666;
            }
            /* Today date styling */
            QCalendarWidget QTableView QTableCornerButton::section:pressed {
                background-color: #0078D4;
            }
        """)
        
        # Time picker
        time_widget = QWidget()
        time_layout = QHBoxLayout(time_widget)
        
        class CustomTimeEdit(QTimeEdit):
            def __init__(self):
                super().__init__()
                self.setDisplayFormat("HH : mm : ss")
                self.setMinimumWidth(200)
                self.setFixedHeight(40)
                self.setStyleSheet("""
                    QTimeEdit {
                        background-color: rgba(32, 32, 32, 0.95);
                        color: white;
                        padding: 5px 35px 5px 10px;
                        border-radius: 5px;
                        min-width: 200px;
                        font-size: 18px;
                        selection-background-color: #0078D4;
                        selection-color: white;
                        border: 1px solid #404040;
                    }
                    QTimeEdit::section {
                        background-color: transparent;
                        color: white;
                        min-width: 40px;
                    }
                    QTimeEdit::up-button {
                        subcontrol-origin: padding;
                        subcontrol-position: right;
                        right: 0px;
                        top: 0px;
                        background-color: transparent;
                        width: 20px;
                        height: 20px;
                        border: none;
                    }
                    QTimeEdit::down-button {
                        subcontrol-origin: padding;
                        subcontrol-position: right;
                        right: 0px;
                        bottom: 0px;
                        background-color: transparent;
                        width: 20px;
                        height: 20px;
                        border: none;
                    }
                    QTimeEdit::up-button:hover, QTimeEdit::down-button:hover {
                        background-color: rgba(255, 255, 255, 0.1);
                    }
                """)

        self.time_edit = CustomTimeEdit()
        
        # Set initial button text and style
        for child in self.time_edit.findChildren(QPushButton):
            if "up" in child.objectName():
                child.setText("▲")
                child.setStyleSheet("""
                    color: white;
                    font-weight: bold;
                    background: transparent;
                    border: none;
                    font-size: 8px;
                """)
            elif "down" in child.objectName():
                child.setText("▼")
                child.setStyleSheet("""
                    color: white;
                    font-weight: bold;
                    background: transparent;
                    border: none;
                    font-size: 8px;
                """)
        
        time_label = QLabel("Time of Birth:")
        time_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 16px;
                font-weight: bold;
                margin-right: 10px;
            }
        """)
        
        time_layout.addStretch()
        time_layout.addWidget(time_label)
        time_layout.addWidget(self.time_edit)
        time_layout.addStretch()
        
        # Navigation
        nav_layout = QHBoxLayout()
        back_btn = ModernButton("◀ Back", "#64748B")
        next_btn = ModernButton("Calculate Age", "#8B5CF6")
        
        back_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        next_btn.clicked.connect(self.calculate_and_show_result)
        
        page_indicator = QLabel("2/3")
        page_indicator.setAlignment(Qt.AlignmentFlag.AlignCenter)
        page_indicator.setStyleSheet("""
            color: #718096;
            font-size: 14px;
            font-weight: bold;
            background: rgba(255, 255, 255, 0.2);
            padding: 5px 15px;
            border-radius: 15px;
        """)
        
        nav_layout.addWidget(back_btn)
        nav_layout.addStretch()
        nav_layout.addWidget(page_indicator)
        nav_layout.addStretch()
        nav_layout.addWidget(next_btn)
        
        container_layout.addWidget(title)
        container_layout.addWidget(self.calendar)
        container_layout.addWidget(time_widget)
        container_layout.addLayout(nav_layout)
        
        layout.addStretch()
        layout.addWidget(container)
        layout.addStretch()
        
        self.stacked_widget.addWidget(picker_widget)

    def create_result_page(self):
        result_widget = QWidget()
        layout = QVBoxLayout(result_widget)
        layout.setSpacing(20)
        
        self.age_label = QLabel()
        self.age_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.age_label.setFont(QFont('Arial', 14))
        
        self.detailed_age_label = QLabel()
        self.detailed_age_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.detailed_age_label.setFont(QFont('Arial', 12))
        
        self.next_birthday_label = QLabel()
        self.next_birthday_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.next_birthday_label.setFont(QFont('Arial', 12))
        
        self.celebration_label = QLabel()
        self.celebration_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.celebration_label.setFont(QFont('Arial', 24, QFont.Weight.Bold))
        
        # Navigation buttons
        nav_layout = QHBoxLayout()
        
        back_btn = QPushButton("◀ Back")
        back_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        
        home_btn = QPushButton("🏠 Home")
        home_btn.clicked.connect(self.go_home)
        home_btn.setStyleSheet("""
            QPushButton {
                background-color: #48BB78;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #38A169;
            }
        """)
        
        # Add page indicator
        page_indicator = QLabel("Page 3/3")
        page_indicator.setAlignment(Qt.AlignmentFlag.AlignCenter)
        page_indicator.setStyleSheet("color: #718096;")
        
        nav_layout.addWidget(back_btn)
        nav_layout.addStretch()
        nav_layout.addWidget(page_indicator)
        nav_layout.addStretch()
        nav_layout.addWidget(home_btn)
        
        layout.addStretch()
        layout.addWidget(self.age_label)
        layout.addWidget(self.detailed_age_label)
        layout.addWidget(self.next_birthday_label)
        layout.addWidget(self.celebration_label)
        layout.addLayout(nav_layout)
        layout.addStretch()
        
        self.stacked_widget.addWidget(result_widget)

    def calculate_and_show_result(self):
        self.birth_time = self.time_edit.time()
        self.stacked_widget.setCurrentIndex(2)
        self.update_age()

    def update_age(self):
        if self.stacked_widget.currentIndex() != 2:
            return
            
        birth_date = self.calendar.selectedDate().toPyDate()
        birth_datetime = datetime.datetime.combine(
            birth_date,
            datetime.time(
                self.birth_time.hour(),
                self.birth_time.minute(),
                self.birth_time.second()
            )
        )
        current_date = datetime.datetime.now()
        
        # Calculate years and months
        years = current_date.year - birth_date.year
        months = current_date.month - birth_date.month
        
        if months < 0:
            years -= 1
            months += 12
        elif months == 0 and current_date.day < birth_date.day:
            years -= 1
            months = 11
            
        # Calculate days and time
        delta = current_date - birth_datetime
        days = delta.days
        seconds = delta.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        
        # Check if it's birthday
        is_birthday = (current_date.month == birth_date.month and 
                      current_date.day == birth_date.day)
        
        if is_birthday:
            self.celebration_label.setText("🎉 Happy Birthday! 🎂")
            self.next_birthday_label.setText("")
            self.celebration_label.setStyleSheet("""
                color: #FF4081;
                font-size: 32px;
                background-color: rgba(255, 64, 129, 0.1);
                padding: 20px;
                border-radius: 15px;
                border: 2px solid #FF4081;
            """)
            
            # Create confetti effect
            for _ in range(50):  # Create 50 confetti particles
                QTimer.singleShot(random.randint(0, 2000), self.create_confetti)
            
            # Schedule new confetti every few seconds
            def create_confetti_batch():
                if self.stacked_widget.currentIndex() == 2:  # Only if still on result page
                    for _ in range(20):
                        self.create_confetti()
            
            # Create new confetti every 3 seconds
            self.confetti_timer = QTimer()
            self.confetti_timer.timeout.connect(create_confetti_batch)
            self.confetti_timer.start(3000)
        else:
            self.celebration_label.setText("")
            if hasattr(self, 'confetti_timer'):
                self.confetti_timer.stop()
            # Calculate next birthday
            next_birthday = datetime.date(current_date.year, birth_date.month, birth_date.day)
            if next_birthday < current_date.date():
                next_birthday = datetime.date(current_date.year + 1, birth_date.month, birth_date.day)
            days_to_birthday = (next_birthday - current_date.date()).days
            
            self.next_birthday_label.setText(
                f"Next birthday in: {days_to_birthday} days\n"
                f"({next_birthday.strftime('%B %d, %Y')})"
            )
        
        # Update age display
        time_str = (
            f"{years} years, {months} months, {days} days\n"
            f"{hours} hours, {minutes} minutes, {seconds} seconds"
        )
        
        self.age_label.setText("Your age is:")
        self.detailed_age_label.setText(time_str)
        self.detailed_age_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: white;
                padding: 20px;
                background-color: rgba(45, 55, 72, 0.8);
                border-radius: 10px;
                margin: 10px;
            }
        """)

    def style_window(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F7FAFC;
            }
            QPushButton {
                background-color: #4299E1;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #3182CE;
            }
            QCalendarWidget {
                background-color: white;
                border-radius: 10px;
            }
            QTimeEdit {
                padding: 5px;
                border: 1px solid #E2E8F0;
                border-radius: 5px;
                min-width: 100px;
            }
        """)

    def go_home(self):
        """Reset and return to home page"""
        self.stacked_widget.setCurrentIndex(0)
        self.time_edit.setTime(QTime(0, 0, 0))
        self.calendar.setSelectedDate(QDateTime.currentDateTime().date())

    def create_confetti(self):
        confetti_label = QLabel(self)
        confetti_label.setFixedSize(10, 10)
        color = random.choice(['#FF4081', '#FF9800', '#FFEB3B', '#4CAF50', '#2196F3', '#9C27B0'])
        confetti_label.setStyleSheet(f"""
            background-color: {color};
            border-radius: 5px;
        """)
        
        # Random starting position at the top
        x = random.randint(0, self.width())
        confetti_label.move(x, -10)
        confetti_label.show()
        
        # Create falling animation
        animation = QPropertyAnimation(confetti_label, b"pos")
        animation.setDuration(random.randint(1500, 3000))
        animation.setStartValue(QPoint(x, -10))
        animation.setEndValue(QPoint(x + random.randint(-100, 100), self.height() + 10))
        animation.finished.connect(confetti_label.deleteLater)
        animation.start()

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        calculator = AgeCalculator()
        calculator.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        input("Press Enter to exit...")