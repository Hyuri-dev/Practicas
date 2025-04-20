import sqlite3
from tkinter import messagebox as mb


class Usuarios:
    
    #Creamos las funciones del crud, iniciando con la conexion a la base de datos
    def abrir_conexion(self):
        conexion = sqlite3.connect("usuarios.db")
        print("conexion creada")
        return conexion
    
    def insertar_usuario(self, datos):
        conn = self.abrir_conexion()
        cursor = conn.cursor()
        sql = "INSERT INTO usuario (usuario, contraseña) VALUES (?,?)"
        cursor.execute(sql, datos)
        id_usuario = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        mb.showinfo("Información", "Registro guardado con éxito")
        return id_usuario
    
    def consultar_usuarios(self):
        conn = self.abrir_conexion()
        cursor = conn.cursor()
        sql ="SELECT id, usuario, contraseña FROM usuario"
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return[]
        finally:
            cursor.close()
            conn.close()
    
    def eliminar_usuario(self, user_id):
        conn = self.abrir_conexion()
        cursor = conn.cursor()
        sql = "DELETE FROM usuario WHERE id = ?"
        id = (user_id,)
        try:
            cursor.execute(sql, id)
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            mb.showerror("Error", f"Error al eliminar usuario: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
            
    def actualizar_usuario(self, datos):
        conn = self.abrir_conexion()
        cur = conn.cursor()
        sql = "UPDATE USUARIO SET usuario = ?, contraseña = ? WHERE id = ?"
        try:
            cur.execute(sql, datos)
            conn.commit()
            return cur.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False
        finally:
            cur.close()
            conn.close()

