import sys
import json
import re
import openai
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, 
    QPushButton, QLabel, QLineEdit, QTextEdit, QDialog, QFormLayout, 
    QMessageBox, QRadioButton, QButtonGroup, QComboBox
)
from PyQt5.QtCore import QTimer

class ConfigDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Configuração')
        self.setGeometry(150, 150, 400, 200)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        self.layout = QFormLayout()
        self.api_key_input = QLineEdit()
        self.api_key_input.setStyleSheet("background-color: #2c2c2c; color: white;")

        self.save_button = QPushButton('Salvar')
        self.save_button.setStyleSheet("background-color: #2c2c2c; color: white;")
        self.save_button.clicked.connect(self.save_api_key)

        self.layout.addRow('Chave API:', self.api_key_input)
        self.layout.addRow(self.save_button)
        self.setLayout(self.layout)

        self.load_api_key()

    def load_api_key(self):
        try:
            with open('config.json', 'r', encoding='utf-8') as file:
                config = json.load(file)
                self.api_key_input.setText(config.get('api_key', ''))
        except FileNotFoundError:
            pass

    def save_api_key(self):
        api_key = self.api_key_input.text().strip()
        with open('config.json', 'w', encoding='utf-8') as file:
            json.dump({'api_key': api_key}, file)
        openai.api_key = api_key
        self.accept()
        
# Classe para exibir as recomendações e efeitos adversos
class IndicationsDialog(QDialog):
    def __init__(self, classe, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f'Indicações para {classe}')
        self.setGeometry(300, 300, 600, 400)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        layout = QVBoxLayout()

        # Carregar informações do JSON
        with open('classes.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Acessar a classe correta no JSON
        class_data = data.get(classe, None)
        if class_data:
            # Mostrar medicação
            medication_label = QLabel(class_data)
            medication_label.setStyleSheet("font-size: 16px; padding: 10px;")
            layout.addWidget(medication_label)

            # Botões de Recomendações e Adversos
            buttons_layout = QHBoxLayout()
            recomendacoes_button = QPushButton('Recomendações')
            recomendacoes_button.setStyleSheet("background-color: #2c2c2c; color: white;")
            recomendacoes_button.clicked.connect(lambda: self.show_details('recomendacoes', data))
            
            adversos_button = QPushButton('Adversos')
            adversos_button.setStyleSheet("background-color: #2c2c2c; color: white;")
            adversos_button.clicked.connect(lambda: self.show_details('adversos', data))

            buttons_layout.addWidget(recomendacoes_button)
            buttons_layout.addWidget(adversos_button)
            
            layout.addLayout(buttons_layout)
        else:
            error_label = QLabel("Dados para a classe não encontrados ou formato incorreto.")
            error_label.setStyleSheet("font-size: 16px; padding: 10px;")
            layout.addWidget(error_label)

        # Botão para fechar
        close_button = QPushButton('Fechar')
        close_button.setStyleSheet("background-color: #2c2c2c; color: white;")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)

    def show_details(self, key, data):
        details = data.get(key, f'{key.capitalize()} não encontrado')
        QMessageBox.information(self, key.capitalize(), details)


class IndicationsDialog(QDialog):
    def __init__(self, classe, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f'Indicações para {classe}')
        self.setGeometry(300, 300, 600, 400)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        layout = QVBoxLayout()

        # Carregar informações do JSON
        with open('classes.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Mapeamento das classes
        class_mapping = {
            "Classe I: Forma ocular pura": "classeI",
            "Classe IIa: Leve generalizada, predomínio apendiculares e axiais": "classeII",
            "Classe IIb: Leve generalizada, predomínio musculatura orofaríngea e respiratória": "classeII",
            "Classe IIIa: Moderada generalizada, predomínio apendiculares e axiais": "classeIII",
            "Classe IIIb: Moderada generalizada, predomínio musculatura orofaríngea e respiratória": "classeIII",
            "Classe IVa: Forma severa, predomínio apendiculares e axiais": "classeIV",
            "Classe IVb: Forma severa, predomínio musculatura orofaríngea e respiratória": "classeIV",
            "Classe V: Necessidade de intubação": "classeV"
        }

        # Obter a chave correta no JSON
        json_key = class_mapping.get(classe, None)

        if json_key and json_key in data:
            # Mostrar medicação
            medication_label = QLabel(f"Medicação para {classe}: {data[json_key]}")
            medication_label.setStyleSheet("font-size: 16px; padding: 10px;")
            layout.addWidget(medication_label)

            # Botões de Recomendações e Adversos
            buttons_layout = QHBoxLayout()
            recomendacoes_button = QPushButton('Recomendações')
            recomendacoes_button.setStyleSheet("background-color: #2c2c2c; color: white;")
            recomendacoes_button.clicked.connect(lambda: self.show_details('recomendacoes', data))
            
            adversos_button = QPushButton('Adversos')
            adversos_button.setStyleSheet("background-color: #2c2c2c; color: white;")
            adversos_button.clicked.connect(lambda: self.show_details('adversos', data))

            buttons_layout.addWidget(recomendacoes_button)
            buttons_layout.addWidget(adversos_button)
            
            layout.addLayout(buttons_layout)
        else:
            error_label = QLabel("Dados para a classe não encontrados ou formato incorreto.")
            error_label.setStyleSheet("font-size: 16px; padding: 10px;")
            layout.addWidget(error_label)

        # Botão para fechar
        close_button = QPushButton('Fechar')
        close_button.setStyleSheet("background-color: #2c2c2c; color: white;")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)

    def show_details(self, key, data):
        details = data.get(key, f'{key.capitalize()} não encontrado')
        QMessageBox.information(self, key.capitalize(), details)




# Definindo a classe MGFAQueryDialog
class MGFAQueryDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Escala MGFA')
        self.setGeometry(300, 300, 400, 200)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        layout = QVBoxLayout()

        question_label = QLabel('Deseja prosseguir para a escala MGFA?')
        question_label.setStyleSheet("font-size: 18px; padding: 20px;")

        buttons_layout = QHBoxLayout()
        yes_button = QPushButton('Sim')
        yes_button.setStyleSheet("background-color: #2c2c2c; color: white;")
        yes_button.clicked.connect(self.accept)  # Sinal de aceitação

        no_button = QPushButton('Não')
        no_button.setStyleSheet("background-color: #2c2c2c; color: white;")
        no_button.clicked.connect(self.reject)  # Sinal de rejeição

        buttons_layout.addWidget(yes_button)
        buttons_layout.addWidget(no_button)

        layout.addWidget(question_label)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

class MGFAFormDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Escala MGFA')
        self.setGeometry(300, 300, 600, 500)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()

        # Ptose (olhar para cima facilmente)
        self.ptose_combo = QComboBox()
        self.ptose_combo.addItems([
            "> 45 segundos (3)", 
            "11–45 segundos (2)", 
            "1–10 segundos (1)", 
            "Imediata (0)"
        ])
        self.form_layout.addRow(QLabel('Ptose (olhar para cima facilmente):'), self.ptose_combo)

        # Visão dupla (olhar fixo lateral)
        self.visao_dupla_combo = QComboBox()
        self.visao_dupla_combo.addItems([
            "> 45 segundos (4)", 
            "11–45 segundos (3)", 
            "1–10 segundos (1)", 
            "Imediata (0)"
        ])
        self.form_layout.addRow(QLabel('Visão dupla (olhar fixo lateral):'), self.visao_dupla_combo)

        # Fechamento dos olhos
        self.fechamento_olhos_combo = QComboBox()
        self.fechamento_olhos_combo.addItems([
            "Normal (0)", 
            "Fraqueza leve (1)", 
            "Fraqueza moderada (2)", 
            "Fraqueza grave (0)"
        ])
        self.form_layout.addRow(QLabel('Fechamento dos olhos:'), self.fechamento_olhos_combo)

        # Fala
        self.fala_combo = QComboBox()
        self.fala_combo.addItems([
            "Normal (0)",
            "Gagueira intermitente ou fala nasal (2)",
            "Gagueira constante ou fala nasal que pode ser compreendida (4)",
            "Dificuldade no entendimento da fala (6)"
        ])
        self.form_layout.addRow(QLabel('Fala (História do paciente):'), self.fala_combo)

        # Mastigação
        self.mastigacao_combo = QComboBox()
        self.mastigacao_combo.addItems([
            "Normal (0)",
            "Fadiga com alimentos sólidos (2)",
            "Fadiga com alimentos moles (4)",
            "Tubo gástrico (6)"
        ])
        self.form_layout.addRow(QLabel('Mastigação (História do paciente):'), self.mastigacao_combo)

        # Deglutição
        self.degluticao_combo = QComboBox()
        self.degluticao_combo.addItems([
            "Normal (0)",
            "Dispneia de esforço (2)",
            "Dispneia em repouso (4)",
            "Ventilador dependente (9)"
        ])
        self.form_layout.addRow(QLabel('Deglutição (História do paciente):'), self.degluticao_combo)

        # Respiração
        self.respiracao_combo = QComboBox()
        self.respiracao_combo.addItems([
            "Normal (0)",
            "Fraqueza leve (1)",
            "Fraqueza moderada (~50% fraca ± 15%) (4)",
            "Fraqueza grave (0)"
        ])
        self.form_layout.addRow(QLabel('Respiração (consequência da MG):'), self.respiracao_combo)

        # Flexão ou extensão de pescoço
        self.pescoco_combo = QComboBox()
        self.pescoco_combo.addItems([
            "Normal (0)",
            "Fraqueza leve (1)",
            "Fraqueza moderada (~50% fraca ± 15%) (3)",
            "Fraqueza grave (4)"
        ])
        self.form_layout.addRow(QLabel('Flexão ou extensão de pescoço:'), self.pescoco_combo)

        # Abdução de ombros
        self.ombros_combo = QComboBox()
        self.ombros_combo.addItems([
            "Normal (0)",
            "Fraqueza leve (2)",
            "Fraqueza moderada (~50% fraca ± 15%) (4)",
            "Fraqueza grave (5)"
        ])
        self.form_layout.addRow(QLabel('Abdução de ombros:'), self.ombros_combo)

        # Flexão do quadril
        self.quadril_combo = QComboBox()
        self.quadril_combo.addItems([
            "Normal (0)",
            "Fraqueza leve (2)",
            "Fraqueza moderada (~50% fraca ± 15%) (4)",
            "Fraqueza grave (5)"
        ])
        self.form_layout.addRow(QLabel('Flexão do quadril:'), self.quadril_combo)

        self.submit_button = QPushButton('Calcular Pontuação')
        self.submit_button.setStyleSheet("background-color: #2c2c2c; color: white;")
        self.submit_button.clicked.connect(self.calculate_mgfa_score)

        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def calculate_mgfa_score(self):
        # Coleta de todas as pontuações das ComboBoxes
        ptose_score = int(self.ptose_combo.currentText()[-2])
        visao_dupla_score = int(self.visao_dupla_combo.currentText()[-2])
        fechamento_olhos_score = int(self.fechamento_olhos_combo.currentText()[-2])

        fala_score = int(self.fala_combo.currentText()[-2])
        mastigacao_score = int(self.mastigacao_combo.currentText()[-2])
        degluticao_score = int(self.degluticao_combo.currentText()[-2])
        respiracao_score = int(self.respiracao_combo.currentText()[-2])

        pescoco_score = int(self.pescoco_combo.currentText()[-2])
        ombros_score = int(self.ombros_combo.currentText()[-2])
        quadril_score = int(self.quadril_combo.currentText()[-2])

        # Classificação ocular (Classe I)
        if (ptose_score <= 2 and visao_dupla_score <= 2 and fechamento_olhos_score <= 2 and 
            fala_score == 0 and mastigacao_score == 0 and degluticao_score == 0 and 
            respiracao_score == 0 and pescoco_score == 0 and ombros_score == 0 and quadril_score == 0):
            mgfa_class = "Classe I: Forma ocular pura"
        # Classificação severa (Classe V)
        elif respiracao_score == 9:
            mgfa_class = "Classe V: Necessidade de intubação"
        else:
            # Contagem dos sintomas leves, moderados e graves
            leves_apendiculares_axiais = sum([score <= 2 for score in [pescoco_score, ombros_score, quadril_score]])
            leves_orofaringeos_respiratorios = sum([score <= 2 for score in [fala_score, mastigacao_score, degluticao_score, respiracao_score]])

            moderados_apendiculares_axiais = sum([3 <= score <= 4 for score in [pescoco_score, ombros_score, quadril_score]])
            moderados_orofaringeos_respiratorios = sum([3 <= score <= 4 for score in [fala_score, mastigacao_score, degluticao_score, respiracao_score]])

            severos_apendiculares_axiais = sum([score >= 4 for score in [pescoco_score, ombros_score, quadril_score]])
            severos_orofaringeos_respiratorios = sum([score >= 4 for score in [fala_score, mastigacao_score, degluticao_score, respiracao_score]])

            if leves_apendiculares_axiais > leves_orofaringeos_respiratorios:
                mgfa_class = "Classe IIa: Leve generalizada, predomínio apendiculares e axiais"
            elif leves_orofaringeos_respiratorios >= leves_apendiculares_axiais:
                mgfa_class = "Classe IIb: Leve generalizada, predomínio musculatura orofaríngea e respiratória"

            elif moderados_apendiculares_axiais > moderados_orofaringeos_respiratorios:
                mgfa_class = "Classe IIIa: Moderada generalizada, predomínio apendiculares e axiais"
            elif moderados_orofaringeos_respiratorios >= moderados_apendiculares_axiais:
                mgfa_class = "Classe IIIb: Moderada generalizada, predomínio musculatura orofaríngea e respiratória"

            elif severos_apendiculares_axiais > severos_orofaringeos_respiratorios:
                mgfa_class = "Classe IVa: Forma severa, predomínio apendiculares e axiais"
            else:
                mgfa_class = "Classe IVb: Forma severa, predomínio musculatura orofaríngea e respiratória"
        
        # Se a pontuação total for 0, o paciente não tem a doença
        if (ptose_score == 0 and visao_dupla_score == 0 and fechamento_olhos_score == 0 and 
            fala_score == 0 and mastigacao_score == 0 and degluticao_score == 0 and 
            respiracao_score == 0 and pescoco_score == 0 and ombros_score == 0 and quadril_score == 0):
            mgfa_class = "Nenhuma classe: O paciente não apresenta sinais de MG."

        # Soma das pontuações (para exibir)
        total_score = (
            ptose_score + visao_dupla_score + fechamento_olhos_score + fala_score +
            mastigacao_score + degluticao_score + respiracao_score + 
            pescoco_score + ombros_score + quadril_score
        )

        self.show_results(total_score, mgfa_class)

    def show_results(self, total_score, mgfa_class):
        result_dialog = QDialog(self)
        result_dialog.setWindowTitle('Resultado MGFA')
        result_dialog.setGeometry(300, 300, 400, 300)
        result_dialog.setStyleSheet("background-color: #1e1e1e; color: white;")
        
        layout = QVBoxLayout()

        # Mostrar a pontuação e a classe
        result_label = QLabel(f"A pontuação total é: {total_score}\nClassificação: {mgfa_class}")
        result_label.setStyleSheet("font-size: 16px; padding: 20px;")
        layout.addWidget(result_label)

        # Botões de Ver Indicações e Fechar
        buttons_layout = QHBoxLayout()
        view_indications_button = QPushButton('Ver Indicações')
        view_indications_button.setStyleSheet("background-color: #2c2c2c; color: white;")
        view_indications_button.clicked.connect(lambda: self.open_indications(mgfa_class, result_dialog))

        close_button = QPushButton('Fechar')
        close_button.setStyleSheet("background-color: #2c2c2c; color: white;")
        close_button.clicked.connect(result_dialog.close)

        buttons_layout.addWidget(view_indications_button)
        buttons_layout.addWidget(close_button)

        layout.addLayout(buttons_layout)

        result_dialog.setLayout(layout)
        result_dialog.exec_()

    def open_indications(self, mgfa_class, parent_dialog):
        # Fecha as janelas de resultados e da escala
        parent_dialog.close()
        self.close()
        # Abre a janela de indicações
        indication_dialog = IndicationsDialog(mgfa_class, self)
        indication_dialog.exec_()


class DocMedChatApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('DocMed Chat')
        self.setGeometry(100, 100, 800, 600)

        self.responses = {}  # Dicionário para salvar as respostas do usuário
        self.load_questions()
        self.load_api_key()
        self.initUI()
        self.consultation_started = False  # Flag para verificar se a consulta foi iniciada

    def load_questions(self):
        with open('questions.json', 'r', encoding='utf-8') as file:
            self.questions = json.load(file)['questions']
        self.current_question_id = 'q1'

    def load_api_key(self):
        try:
            with open('config.json', 'r', encoding='utf-8') as file:
                config = json.load(file)
                openai.api_key = config.get('api_key', '')
        except FileNotFoundError:
            openai.api_key = ''

    def initUI(self):
        # Layout principal
        main_layout = QHBoxLayout()

        # Layout da barra lateral
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setSpacing(10)
        sidebar_layout.setContentsMargins(10, 10, 10, 10)

        # Novos botões
        new_query_button = QPushButton('Nova Consulta')
        new_query_button.setStyleSheet("background-color: #2c2c2c; color: white;")
        new_query_button.clicked.connect(self.start_new_query)

        config_button = QPushButton('Configuração')
        config_button.setStyleSheet("background-color: #2c2c2c; color: white;")
        config_button.clicked.connect(self.open_config_dialog)

        logout_button = QPushButton('Sair')
        logout_button.setStyleSheet("background-color: #2c2c2c; color: white;")
        logout_button.clicked.connect(self.close_app)

        sidebar_layout.addWidget(new_query_button)
        sidebar_layout.addWidget(config_button)
        sidebar_layout.addStretch()
        sidebar_layout.addWidget(logout_button)

        # Layout da área do chat
        self.chat_area_layout = QVBoxLayout()
        self.chat_area_layout.setSpacing(20)
        self.chat_area_layout.setContentsMargins(10, 10, 10, 10)

        self.chat_display = QTextEdit()
        self.chat_display.setStyleSheet("font-size: 16px; color: white; background-color: #2c2c2c; border: 1px solid #444444; padding: 10px;")
        self.chat_display.setReadOnly(True)
        self.chat_display.setLineWrapMode(QTextEdit.WidgetWidth)
        self.chat_area_layout.addWidget(self.chat_display)

        self.typing_message = QLabel("")
        self.typing_message.setStyleSheet("font-size: 12px; color: #888888; padding: 5px;")
        self.chat_area_layout.addWidget(self.typing_message)

        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setStyleSheet("background-color: #2c2c2c; color: white;")
        send_button = QPushButton('Enviar')
        send_button.setStyleSheet("background-color: #444444; color: white;")
        send_button.clicked.connect(self.handle_input)
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(send_button)

        self.chat_area_layout.addLayout(input_layout)

        # Adicionar layouts ao layout principal
        main_layout.addLayout(sidebar_layout, 1)
        main_layout.addLayout(self.chat_area_layout, 4)

        # Definir widget principal
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        main_widget.setStyleSheet("background-color: #1e1e1e;")

        self.setCentralWidget(main_widget)

        # Mostrar mensagem de boas-vindas
        self.show_welcome_message()

    def show_welcome_message(self):
        self.chat_display.append("<b>DocMed Chat</b><br><br><b>Bem-vindo!</b> Este sistema é um chatbot programado para auxiliar no descobrimento sobre pacientes com Miastenia Gravis por meio de perguntas e respostas predeterminadas.<br><br>")

    def start_new_query(self):
        if not openai.api_key:
            self.show_api_key_error()
            return
        
        self.consultation_started = True  # Definir a flag como true
        self.responses = {}  # Resetar respostas anteriores
        self.chat_display.clear()  # Limpar a exibição do chat
        self.current_question_id = 'q1'
        self.show_typing_message(self.show_next_question)

    def open_config_dialog(self):
        dialog = ConfigDialog(self)
        dialog.exec_()

    def show_api_key_error(self):
        self.chat_display.append("<b>DocMed Chat</b><br><br><b>Para utilização do sistema é necessário possuir uma chave GPT, favor contatar os desenvolvedores.</b><br><br>")

    def show_typing_message(self, next_function):
        self.typing_message.setText("Sistema está digitando...")
        QTimer.singleShot(2000, lambda: self.hide_typing_message(next_function))

    def hide_typing_message(self, next_function):
        self.typing_message.setText("")
        next_function()

    def show_next_question(self):
        try:
            if self.current_question_id == "end":
                self.save_responses()  # Salvar respostas ao final da consulta
                self.ask_mgfa_scale()  # Perguntar se deseja prosseguir para a escala MGFA
                return

            # Verificar se a chave atual existe no dicionário
            if self.current_question_id not in self.questions:
                raise KeyError(f"A chave {self.current_question_id} não foi encontrada nas perguntas.")

            question = self.questions[self.current_question_id]['question']
            self.add_to_chat(f"Sistema: {question}")

        except KeyError as e:
            print(f"Erro ao acessar a pergunta: {e}")
            self.add_to_chat("Erro ao acessar a pergunta. Por favor, reinicie a consulta.")
        except Exception as e:
            print(f"Erro inesperado: {e}")
            self.add_to_chat("Ocorreu um erro inesperado. Por favor, reinicie a consulta.")

    def handle_input(self):
        user_input = self.input_field.text().strip().lower()
        self.input_field.clear()

        if not self.consultation_started:
            self.add_to_chat(f"Você: {user_input}")
            self.add_to_chat("Sistema: Desculpe, sou um chatbot com respostas predeterminadas e não consigo entender nada além do formato de resposta pré-estabelecido. Por favor, clique em 'Nova Consulta' para iniciar nossa conversa.<br><br>")
            return

        self.add_to_chat(f"Você: {user_input}")

        try:
            current_question = self.questions[self.current_question_id]
        except KeyError as e:
            print(f"Erro ao acessar a pergunta atual: {e}")
            self.add_to_chat("Erro ao acessar a pergunta atual. Por favor, reinicie a consulta.")
            return

        gpt_response, next_question_id = self.ask_question_gpt(current_question, user_input, self.questions)
        
        if next_question_id:
                    gpt_response, next_question_id = self.ask_question_gpt(current_question, user_input, self.questions)
        
        if next_question_id:
            self.show_typing_message(lambda: self.show_response(gpt_response, next_question_id))
        else:
            self.show_typing_message(self.show_invalid_response)

    def show_response(self, response, next_question_id):
        self.add_to_chat(f"Sistema: {response}")
        self.current_question_id = next_question_id
        self.show_typing_message(self.show_next_question)

    def show_invalid_response(self):
        self.add_to_chat("Sistema: Desculpe, sou um chatbot com respostas predeterminadas e não consigo entender nada além do formato de resposta pré-estabelecido.")
        self.show_typing_message(self.show_next_question)

    def add_to_chat(self, message):
        self.chat_display.append(f"{message}<br>")
        self.chat_display.verticalScrollBar().setValue(self.chat_display.verticalScrollBar().maximum())

    def close_app(self):
        self.close()

    def save_responses(self):
        with open('responses.json', 'w', encoding='utf-8') as f:
            json.dump(self.responses, f, ensure_ascii=False, indent=4)

    def ask_question_gpt(self, current_question, user_input, questions):
        try:
            # Obter opções relevantes para a pergunta atual
            current_question_options = questions[self.current_question_id]['options']

            prompt = f"""
            Você é um gerenciador de chatbot programado para auxiliar no descobrimento sobre pacientes com Miastenia Gravis por meio de perguntas e respostas predeterminadas. Seu trabalho é validar a resposta do usuário/médico com base nas opções fornecidas.

            Pergunta atual: {current_question['question']}
            Resposta do usuário: {user_input}
            Opções possíveis:
            {json.dumps(current_question_options, ensure_ascii=False, indent=4)}

            Faça uma comparação fonética da resposta do usuário com as respostas válidas, antes de considerar a resposta inválida.
            Se a resposta do usuário for uma idade, extraia e normalize o valor numérico.
            Se o usuário pedir uma explicação ou não entender a pergunta, explique o que é para ele, e repita novamente a pergunta.
            Valide a resposta do usuário e determine a próxima pergunta com base nas opções fornecidas.
            Se a resposta for válida ou semelhante às opções válidas, retorne a próxima pergunta, o ID da próxima pergunta e a resposta a ser mostrada ao usuário.
            Se a resposta for inválida, indique que a resposta foi inválida.

            Responda estritamente no seguinte formato JSON:
            {{
                "next_question": "Texto da próxima pergunta",
                "next_question_id": "ID da próxima pergunta",
                "response": "Resposta a ser mostrada ao usuário",
                "normalized_response": "Resposta normalizada do usuário"
            }}
            """

            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Você é um assistente de chatbot que faz perguntas ao usuário e valida as respostas com base nas opções fornecidas."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0,
            )

            response_text = response['choices'][0]['message']['content'].strip()

            # Remover notações de bloco de código se existirem
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_match:
                response_text = json_match.group(0)

            # Verificar se a resposta não está vazia
            if not response_text:
                raise ValueError("A resposta do GPT-4 está vazia")

            # Log da resposta recebida para depuração
            print("Resposta do GPT-4:", response_text)

            # Parse the response as JSON
            response_data = json.loads(response_text)

            next_question = response_data.get("next_question")
            next_question_id = response_data.get("next_question_id")
            response_message = response_data.get("response")
            normalized_response = response_data.get("normalized_response")

            # Permitir que next_question seja vazio se next_question_id for "end"
            if next_question_id != "end" and not next_question:
                raise ValueError("Formato da resposta do GPT-4 inválido")

            # Atualiza a resposta do usuário com a resposta normalizada
            self.responses[self.current_question_id] = {"response": normalized_response}

            return response_message, next_question_id

        except openai.error.OpenAIError as e:
            print(f"Erro na API OpenAI: {e}")
            return "Desculpe, houve um erro ao processar sua resposta.", None
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
            print("Texto da resposta:", response_text)  # Log da resposta para verificar o conteúdo
            return "Desculpe, houve um erro ao processar sua resposta.", None
        except ValueError as e:
            print(f"Erro no formato da resposta: {e}")
            return "Desculpe, houve um erro ao processar sua resposta.", None
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return "Desculpe, houve um erro ao processar sua resposta.", None

    # Novo método para perguntar se deseja continuar para a escala MGFA em uma nova janela
    def ask_mgfa_scale(self):
        dialog = MGFAQueryDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self.open_mgfa_form()
        else:
            self.end_consultation()

    # Método para abrir a janela da escala MGFA
    def open_mgfa_form(self):
        form_dialog = MGFAFormDialog(self)
        form_dialog.exec_()

    # Método para iniciar a escala MGFA
    def start_mgfa_scale(self):
        self.add_to_chat("Sistema: Iniciando a escala MGFA...")
        self.current_question_id = 'mgfa_q1'  # Supondo que as perguntas da escala MGFA comecem com 'mgfa_q1'
        self.show_typing_message(self.show_next_question)

    # Método para encerrar a consulta
    def end_consultation(self):
        self.add_to_chat("Sistema: Consulta encerrada. Obrigado por usar o DocMed Chat.")
        self.consultation_started = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DocMedChatApp()
    window.show()
    sys.exit(app.exec_())
