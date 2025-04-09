workspace {
    model {
        user = person "Пользователь" "Пользователь социальной сети."
        admin = person "Администратор" "Администратор социальной сети."
        notificationSystem = softwareSystem "Система уведомлений" "External"
        authSystem = softwareSystem "Система аутентификации" "External"

        socialNetwork = softwareSystem "Социальная сеть" {
            webApp = container "Веб-приложение" "React"
            apiGateway = container "API Gateway" "FastAPI"
            userService = container "Сервис пользователей" "Python, FastAPI" {
                -> authSystem "Получает JWT токены через /login"
            }
            wallService = container "Сервис стены" "Python, FastAPI"
            messagingService = container "Сервис сообщений" "Python, FastAPI, WebSocket"
            database = container "База данных" "PostgreSQL 14" 
            notificationService = container "Сервис уведомлений" "Python, Flask"
        }

        user -> webApp "Взаимодействует с"
        admin -> webApp "Взаимодействует с"
        webApp -> apiGateway "Отправляет запросы HTTP"
        apiGateway -> userService "Перенаправляет /register, /login, /users" "HTTP"
        apiGateway -> wallService "Перенаправляет /posts" "HTTP"
        userService -> database "Читает/записывает пользователей" "PostgreSQL"
        wallService -> database "Читает/записывает записи" "PostgreSQL"
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
        dynamic socialNetwork "CreatePost" "Создание записи" {
            user -> webApp "Создаёт запись"
            webApp -> apiGateway "POST /posts"
            apiGateway -> wallService "Передаёт данные"
            wallService -> database "Сохраняет запись"
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