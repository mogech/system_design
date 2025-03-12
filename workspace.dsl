workspace {

    model {
        #Пользователи
        user = person "Пользователь" "Пользователь социальной сети."
        admin = person "Администратор" "Администратор социальной сети."

        #Внешние системы
        notificationSystem = softwareSystem "Система уведомлений" "Отправляет уведомления (email, push)" "External"
        authSystem = softwareSystem "Система аутентификации" "Обрабатывает OAuth-аутентификацию" "External"

        socialNetwork = softwareSystem "Социальная сеть" "Позволяет пользователям публиковать записи и отправлять сообщения." {
            webApp = container "Веб-приложение" "Графический интерфейс социальной сети" "React, Мобильное приложение"
            apiGateway = container "API" "Обрабатывает все API-запросы" "Spring Cloud Gateway"
            userService = container "Сервис пользователей" "Управляет регистрацией и поиском пользователей" "Python, Flask"
            wallService = container "Сервис стены" "Управляет записями на стене" "Python, Flask"
            messagingService = container "Сервис сообщений" "Обрабатывает чат в реальном времени" "Python, FastAPI, WebSocket"
            database = container "База данных" "Хранит пользователей, записи и сообщения" "PostgreSQL"
            notificationService = container "Сервис уведомлений" "Отправляет пользователям уведомления" "Python, Flask"
        }

        #Взаимодействие пользователей с системой
        user -> socialNetwork "Использует"
        admin -> socialNetwork "Модерирует"
        socialNetwork -> notificationSystem "Отправляет уведомления через"
        socialNetwork -> authSystem "Аутентифицируется через"

        #Взаимодействие контейнеров
        user -> webApp "Взаимодействует с"
        admin -> webApp "Взаимодействует с"
        webApp -> apiGateway "Отправляет API-запросы в" "HTTPS"
        apiGateway -> userService "Перенаправляет запросы пользователей в" "HTTPS"
        apiGateway -> wallService "Перенаправляет запросы к стене в" "HTTPS"
        apiGateway -> messagingService "Перенаправляет запросы чата в" "HTTPS"

        #Взаимодействие сервисов с базой данных
        userService -> database "Читает/Записывает данные пользователей" "SQL"
        wallService -> database "Читает/Записывает данные стены" "SQL"
        messagingService -> database "Читает/Записывает сообщения" "SQL"

        #Сообщения
        messagingService -> user "Отправляет сообщения в реальном времени" "WebSocket"
        apiGateway -> messagingService "Перенаправляет запросы на получение сообщений" "HTTPS"

        #Уведомления
        notificationService -> notificationSystem "Отправляет уведомления через" "HTTPS"
        wallService -> notificationService "Триггерит уведомления о записях на стене" "HTTPS"
        messagingService -> notificationService "Триггерит уведомления о сообщениях" "HTTPS"
    }

    views {
        systemContext socialNetwork "SystemContext" {
            include *
            autoLayout
        }

        container socialNetwork "Containers" {
            include *
            autoLayout
        }

        styles {
            element "Person" {
                shape Person
                background #C0CE8B
            }
            element "External" {
                background #8F8BCE
            }
            element "Container" {
                background #72A6DB
                color #ffffff
            }
        }
    }
}