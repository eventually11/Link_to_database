CREATE TABLE "ods_saas_partner_order" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "task_id" INTEGER NOT NULL,
    "tenant" INTEGER NOT NULL,
    "order_id" INTEGER NOT NULL,
    "sender" INTEGER,
    "hub" INTEGER,
    "zone" INTEGER,
    "flow" INTEGER,
    "task_pool" INTEGER,
    "partner" INTEGER,
    "title" INTEGER,
    "content" INTEGER,
    "date" TIME,
    "time_slot" VARCHAR(50),
    "type" INTEGER,
    "service_time" INTEGER,
    "start" VARCHAR(255),
    "end" VARCHAR(255),
    "service_fee" DECIMAL(10, 2),
    "items" INTEGER,
    "start_task_validation" INTEGER,
    "end_task_validation" INTEGER,
    "status_code" INTEGER,
    "status_group" INTEGER
);
