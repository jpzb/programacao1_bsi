import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QColor, QPolygon, QTransform
from PyQt5.QtCore import Qt, QTimer, QRect, QPoint


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        # Colocando o título da janela e o tamanho e posição na tela 
        self.setWindowTitle("Formas Geométricas")
        self.setGeometry(500, 200, 1000, 700)
        self.setStyleSheet("background-color: black;")
        
        # Define uma lista de formas geométricas com atributos como tipo, posição, velocidade, ângulo e cor
        self.formas = [
            {
                "type": "rect", 
                "rect": QRect(500, 350, 50, 50), 
                "dx": 0, 
                "dy": 0, 
                "angle": 0, 
                "d_angle": 1, 
                "color": QColor(255, 0, 0)
            },
            {
                "type": "rect", 
                "rect": QRect(100, 370, 100, 150), 
                "dx": 12, 
                "dy": 12, 
                "angle": 0, 
                "d_angle": 4, 
                "color": QColor(255, 0, 255)
            },
            {
                "type": "ellipse", 
                "rect": QRect(200, 150, 150, 150), 
                "dx": 3, 
                "dy": 2, 
                "angle": 0, 
                "d_angle": -3, 
                "color": QColor(0, 255, 0)
            },
            {
                "type": "ellipse", 
                "rect": QRect(600, 500, 50, 50), 
                "dx": 6, 
                "dy": 2, 
                "angle": 0, 
                "d_angle": -1, 
                "color": QColor(255, 255, 0)
            },
            {
                "type": "triangle", 
                "points": [QPoint(400, 300), QPoint(450, 350), QPoint(350, 350)], 
                "dx": -4, 
                "dy": 4, 
                "angle": 0, 
                "d_angle": -4, 
                "color": QColor(0, 0, 255)
            },
            {
                "type": "triangle", 
                "points": [QPoint(100, 100), QPoint(100, 200), QPoint(200, 200)], 
                "dx": 3, 
                "dy": 6, 
                "angle": 0, 
                "d_angle": -1, 
                "color": QColor(0, 255, 255)
            }
        ]

        # Criando um timer de 30 milisegundos 
        self.timer = QTimer()
        # Chamando a função para atualizar as posições
        self.timer.timeout.connect(self.atualizar_posicao)
        self.timer.start(30)
    

    def atualizar_posicao(self):
        for forma in self.formas:
            # Atualizando o ângulo da forma e garantindo que não passe de 360 graus
            forma["angle"] = (forma["angle"] + forma["d_angle"]) % 360

            if forma["type"] in ["rect", "ellipse"]:
                rect = forma["rect"]

                # Movendo a forma para "dx" pixeis horizontalmente
                rect.moveLeft(rect.left() + forma["dx"])
                
                # Movendo a forma para "dy" pixeis verticalmente
                rect.moveTop(rect.top() + forma["dy"])
                
                # Inverte a direção horizontal se atingir as bordas da janela
                if rect.left() <= 0 or rect.right() >= self.width():
                    forma["dx"] = -forma["dx"]

                # Inverte a direção vertical se atingir as bordas da janela
                if rect.top() <= 0 or rect.bottom() >= self.height():
                    forma["dy"] = -forma["dy"]

            elif forma["type"] == "triangle":
                points = forma["points"]
                # Atualizando a posição dos pontos do triângulo

                # Verificação horizontal para caso atinja a borda 
                hit_horizontal = False
                for point in points:
                    point.setX(point.x() + forma["dx"])
                    if point.x() <= 0 or point.x() >= self.width():
                        hit_horizontal = True
                if hit_horizontal:
                    forma["dx"] = -forma["dx"]

                # Verificação vertical para caso atinja a borda 
                hit_vertical = False
                for point in points:
                    point.setY(point.y() + forma["dy"])
                    if point.y() <= 0 or point.y() >= self.height():
                        hit_vertical = True
                if hit_vertical:
                    forma["dy"] = -forma["dy"]
                
        self.update() # Atualizando a tela


    def paintEvent(self, event):
        painter = QPainter(self)
        
        for forma in self.formas:
            painter.save()

            # Definindo a cor do preenchimento da forma
            painter.setBrush(QBrush(forma["color"], Qt.SolidPattern))
            
            if forma["type"] == "rect" or forma["type"] == "ellipse":
                # Calcula o centro da forma
                center = forma["rect"].center() 

                # Move a origem do sistema de coordenadas para o centro
                painter.translate(center)

                # Rotaciona o sistema de coordenadas pelo ângulo
                painter.rotate(forma["angle"])  

                # Move a origem de volta para a posição original
                painter.translate(-center)  

                if forma["type"] == "rect":
                    # Desenha o retângulo rotacionado
                    painter.drawRect(forma["rect"])
                else:
                    # Desenha a elipse rotacionado
                    painter.drawEllipse(forma["rect"])
            elif forma["type"] == "triangle":
                # Cria um QPolygon a partir dos pontos do triângulo
                points = QPolygon(forma["points"])  

                # Calcula o centro do retângulo delimitador do triângulo
                center = points.boundingRect().center()  

                # Cria um objeto QTransform para aplicar transformações
                transform = QTransform()  

                # Move a origem do sistema de coordenadas para o centro
                transform.translate(center.x(), center.y())  

                # Rotaciona o sistema de coordenadas pelo ângulo
                transform.rotate(forma["angle"])  

                # Move a origem de volta para a posição original
                transform.translate(-center.x(), -center.y()) 

                # Aplica a transformação aos pontos do triângulo
                transformed_points = transform.map(points) 

                # Desenha o triângulo rotacionado 
                painter.drawPolygon(transformed_points)  
            
            painter.restore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JanelaPrincipal()
    window.show()
    sys.exit(app.exec_())
