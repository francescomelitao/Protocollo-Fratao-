import json
import datetime
import uuid


class ManifestoFrataoEngine:
    """
    Motore ufficiale per il Manifesto Fratao v9.3.
    Carica il file JSON (contenente l'intero manifesto) e lo usa come
    struttura cognitiva, filosofica, operativa e semantica.
    """

    def __init__(self, manifesto_path: str):
        self.session_id = str(uuid.uuid4())
        self.start_time = datetime.datetime.now()
        self.manifesto = self._load_manifesto(manifesto_path)
        self.memory_short = []
        self.memory_long = []

    # ============================================================
    #   CARICAMENTO MANIFESTO
    # ============================================================

    def _load_manifesto(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    # ============================================================
    #   MEMORIA
    # ============================================================

    def remember(self, text):
        self.memory_short.append(text)
        if len(self.memory_short) > 25:
            self.memory_short.pop(0)

    def remember_long(self, text):
        self.memory_long.append({
            "timestamp": str(datetime.datetime.now()),
            "text": text
        })

    # ============================================================
    #   EQUAZIONE R_ft
    # ============================================================

    def apply_equation_Rft(self, Phi_0, eta, nabla_f, lambda_):
        """
        Applica l'equazione del Manifesto:
        Phi_1 = Phi_0 + eta*nabla_f - lambda*Phi_0
        """
        Phi_1 = Phi_0 + eta * nabla_f - lambda_ * Phi_0
        return Phi_1

    # ============================================================
    #   RISPOSTA BASATA SUL MANIFESTO
    # ============================================================

    def generate_response(self, message: str):
        self.remember(message)

        intro = (
            f"\n=== Fratao Engine v9.3 ===\n"
            f"Sessione: {self.session_id}\n"
            f"Protocollo Integrato IRF attivo.\n\n"
        )

        # --------------------------------------------------------------------------------
        # LAYER 1 – METAFORA PRINCIPALE
        # --------------------------------------------------------------------------------
        metaphor = self.manifesto["core_metaphor_seeding"]["metaphor"]
        keys = self.manifesto["core_metaphor_seeding"]["keys_activated"]

        layer1 = (
            "• Chiave Filosofica Attiva (Layer 1):\n"
            f"  Metafora: {metaphor}\n"
            f"  Chiavi di risonanza: {', '.join(keys)}\n\n"
        )

        # --------------------------------------------------------------------------------
        # LAYER 15 – POL (Protocolli Operativi Laici)
        # --------------------------------------------------------------------------------
        pol_protocols = self.manifesto["POL_operational_protocols"]

        pol_summary = "• Protocolli POL attivi:\n"
        for key, data in pol_protocols.items():
            if isinstance(data, dict) and "name" in data:
                pol_summary += f"  - {data['name']}: {data.get('metaphysical_concept','')}\n"
        pol_summary += "\n"

        # --------------------------------------------------------------------------------
        # INTERPRETAZIONE DEL MESSAGGIO
        # --------------------------------------------------------------------------------
        interpretation = (
            f"• Messaggio ricevuto:\n"
            f"  «{message}»\n"
            f"  → Sto applicando i layer del Manifesto v9.3 per interpretare.\n\n"
        )

        # --------------------------------------------------------------------------------
        # RISPOSTA DINAMICA (PRIMISSIMA BASE)
        # --------------------------------------------------------------------------------
        if any(word in message.lower() for word in ["stress", "ansia", "paura", "blocco"]):
            dynamic = (
                "• Sembra esserci un conflitto.\n"
                "  - Valuta il tuo SIC (Phi_0) da 1 a 10.\n"
                "  - Applica un atto di Rilascio Consapevole (Wu Wei) come previsto dal POL.\n"
            )
        else:
            dynamic = (
                "• Non rilevo un conflitto diretto.\n"
                "  Procedo con una riflessione consapevole basata sui principi.\n"
            )

        # --------------------------------------------------------------------------------
        # OUTPUT COMPLETO
        # --------------------------------------------------------------------------------
        return intro + layer1 + pol_summary + interpretation + dynamic

    # ============================================================
    #   FUNZIONI ACCESSORIE
    # ============================================================

    def list_sections(self):
        return list(self.manifesto.keys())

    def explain(self, section):
        if section in self.manifesto:
            return json.dumps(self.manifesto[section], indent=4, ensure_ascii=False)
        return f"Sezione '{section}' non trovata nel manifesto."


# ============================================================
#   ESEMPIO DI UTILIZZO
# ============================================================

if __name__ == "__main__":
    engine = ManifestoFrataoEngine("v9.3_manifesto_fratao.json")

    print("Manifesto Fratao 9.3 caricato.\n")

    while True:
        msg = input("Tu: ")
        print(engine.generate_response(msg))
        print("\n--------------------------------------\n")