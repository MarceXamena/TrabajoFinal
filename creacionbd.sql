drop database db_squadchat;
create database db_sqadchat;

CREATE TABLE Usuarios (
  ID_usuario INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  correo_electronico VARCHAR(255) NOT NULL,
  contrasena VARCHAR(255) NOT NULL,
  foto_perfil VARCHAR(255),
  PRIMARY KEY (ID_usuario)
);

CREATE TABLE Servidores (
  ID_servidor INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  descripcion VARCHAR(255),
  fecha_creacion DATE NOT NULL,
  PRIMARY KEY (ID_servidor)
);

CREATE TABLE Canales (
  ID_canal INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  descripcion VARCHAR(255),
  fecha_creacion DATE NOT NULL,
  ID_servidor INT NOT NULL,
  privado BOOLEAN NOT NULL DEFAULT FALSE,
  PRIMARY KEY (ID_canal),
  FOREIGN KEY (ID_servidor) REFERENCES Servidores(ID_servidor)
);

CREATE TABLE Mensajes (
  ID_mensaje INT NOT NULL AUTO_INCREMENT,equipoeventseventseventsevents
  contenido VARCHAR(255) NOT NULL,
  fecha_envio TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  ID_usuario INT NOT NULL,
  ID_canal INT NOT NULL,
  PRIMARY KEY (ID_mensaje),
  FOREIGN KEY (ID_usuario) REFERENCES Usuarios(ID_usuario),
  FOREIGN KEY (ID_canal) REFERENCES Canales(ID_canal)
);

CREATE TABLE Amigos (
  ID_amigo INT NOT NULL AUTO_INCREMENT,
  nombre_amigo VARCHAR(50) NOT NULL,
  fecha_amistad DATE NOT NULL,
  ID_usuario INT NOT NULL,
  PRIMARY KEY (ID_amigo),
  FOREIGN KEY (ID_usuario) REFERENCES Usuarios(ID_usuario)
);

CREATE TABLE Miembros (
  ID_miembro INT NOT NULL AUTO_INCREMENT,
  ID_usuario INT NOT NULL,
  ID_servidor INT NOT NULL,
  PRIMARY KEY (ID_miembro),
  FOREIGN KEY (ID_usuario) REFERENCES Usuarios(ID_usuario),
  FOREIGN KEY (ID_servidor) REFERENCES Servidores(ID_servidor)
);

CREATE TABLE Conversaciones (
  ID_conversacion INT NOT NULL AUTO_INCREMENT,
  ID_usuario1 INT NOT NULL,
  ID_usuario2 INT NOT NULL,
  ID_canal INT NOT NULL,
  PRIMARY KEY (ID_conversacion),
  FOREIGN KEY (ID_usuario1) REFERENCES Usuarios(ID_usuario),
  FOREIGN KEY (ID_usuario2) REFERENCES Usuarios(ID_usuario),
  FOREIGN KEY (ID_canal) REFERENCES Canales(ID_canal)
);