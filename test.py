import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Button } from "@/components/ui/button";

export default function EmojiQuoteApp() {
  const [showEmoji, setShowEmoji] = useState(false);

  const handleClick = () => {
    setShowEmoji(true);
    setTimeout(() => setShowEmoji(false), 800); // 애니메이션 후 원래 자리로 복귀
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-6">
      <div className="text-2xl font-bold mb-6">✨ Inspiring Emoji Quote ✨</div>

      <div className="relative h-24 flex items-center justify-center">
        <AnimatePresence>
          {showEmoji && (
            <motion.div
              key="emoji"
              initial={{ opacity: 1, y: 0 }}
              animate={{ opacity: 0, y: -100 }}
              exit={{ opacity: 0, y: 0 }}
              transition={{ duration: 0.8 }}
              className="absolute text-6xl"
            >
              🌟
            </motion.div>
          )}
        </AnimatePresence>
        {!showEmoji && <div className="text-6xl">🌟</div>}
      </div>

      <Button className="mt-6 px-6 py-3 text-lg" onClick={handleClick}>
        Show Inspiration
      </Button>
    </div>
  );
}
