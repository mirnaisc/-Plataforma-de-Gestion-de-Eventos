
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    email VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    rol ENUM('organizador', 'asistente') DEFAULT 'asistente',
    foto_perfil VARCHAR(255)
);

CREATE TABLE eventos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    descripcion TEXT,
    fecha DATE,
    hora TIME,
    lugar VARCHAR(100),
    capacidad INT,
    organizador_id INT,
    FOREIGN KEY (organizador_id) REFERENCES usuarios(id)
);

CREATE TABLE registros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    evento_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (evento_id) REFERENCES eventos(id)
);
