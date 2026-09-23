# ai-mini-project-

import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

class MiniAIAssistant:
    def __init__(self):
        logging.info("Initializing Mini AI Assistant...")

    def get_user_input(self):
        """Step 4: Input Handling Module"""
        print("\n" + "="*50)
        print("🤖 Welcome to Mini AI Assistant!")
        print("="*50)
        user_input = input("Aap kya poochna ya task karwana chahte hain? (Type 'exit' to quit): ")
        return user_input

    def preprocess_input(self, raw_input):
        """Step 2: Preprocessing & Normalization"""
        if not raw_input:
            return ""
        # Extra spaces remove karna aur lowercase mein convert karna
        cleaned = raw_input.strip().lower()
        logging.info(f"Preprocessed input: '{cleaned}'")
        return cleaned

    def core_processing_engine(self, query):
        """Step 3 & 4: Core Processing Logic (Simulated AI Engine)"""
        logging.info("Processing query through AI core engine...")
        
        if not query:
            raise ValueError("Input khali nahi ho sakta!")

        if "hello" in query or "hi" in query:
            return "Hello! Main aapki kya madad kar sakta hoon?"
        elif "python" in query:
            return "Python ek powerful aur beginner-friendly programming language hai jo AI/ML mein sabse zyada use hoti hai."
        elif "time" in query or "date" in query:
            import datetime
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return f"Current system timestamp: {current_time}"
        elif "help" in query:
            return "Aap mujhse 'python', 'hello', ya 'time' ke bare mein pooch sakte hain."
        else:
            return f"Aapka query '{query}' mil gaya hai. Yeh ek simulated AI response hai!"

    def format_output(self, response_text):
        """Step 6: Output Formatting"""
        formatted = f"\n[AI Response]:\n{'-'*30}\n{response_text}\n{'-'*30}"
        return formatted

    def run(self):
        """Step 12: Final Deployment / Run Ready Loop"""
        while True:
            try:
                # 1. Input
                raw_input = self.get_user_input()
                
                if raw_input.strip().lower() == 'exit':
                    print("\nDhanyawad! Phir milte hain. 👋")
                    break

                # 2. Preprocessing
                processed_query = self.preprocess_input(raw_input)

                # 3. Processing with Error Handling (Step 5)
                response = self.core_processing_engine(processed_query)

                # 4. Output Formatting
                print(self.format_output(response))

            except ValueError as ve:
                logging.error(f"Validation Error: {ve}")
                print(f"\n❌ Error: {ve}. Kripya fir se koshish karein.\n")
            except Exception as e:
                logging.critical(f"Unexpected error occurred: {e}")
                print(f"\n⚠️ Kuch galat ho gaya: {e}\n")

if __name__ == "__main__":
    app = MiniAIAssistant()
    app.run()
