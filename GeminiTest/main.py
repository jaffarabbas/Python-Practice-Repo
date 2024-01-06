
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": "what is fish"
  },
  {
    "role": "model",
    "parts": "Fish are aquatic, gill-bearing animals that lack limbs with digits. They form a monophyletic group which contains the living hagfish, lampreys, and cartilaginous and bony fish as well as various extinct related groups. Fish are an important food source for humans and other animals, and they play a crucial role in the Earth's ecosystems.\n\nCharacteristics of Fish:\n\n1. Aquatic: Fish are adapted to live in water, and they obtain oxygen through their gills.\n\n2. Gills: Fish have gills, which are specialized structures that allow them to extract oxygen from water.\n\n3. Lack of Limbs with Digits: Fish do not have limbs with digits (fingers or toes). Instead, they have fins, which help them swim and maintain stability in the water.\n\n4. Scales: Most fish have scales, which provide protection and reduce water resistance.\n\n5. Fins: Fish have fins, which are typically comprised of thin, flexible rays supported by bony or cartilaginous structures. Fins aid in swimming, maneuvering, and balance.\n\n6. Lateral Line System: Fish have a lateral line system, which is a sensory system that helps them detect changes in water pressure and movement. It plays a role in orientation, schooling behavior, and predator avoidance.\n\n7. Respiratory System: Fish have gills, which are specialized respiratory organs that allow them to extract oxygen from water.\n\n8. Circulatory System: Fish typically have a closed circulatory system, meaning that their blood flows through vessels (arteries, veins, and capillaries).\n\n9. Digestive System: Fish have a digestive system that is adapted to their diet. Herbivorous fish have longer digestive tracts to accommodate plant matter, while carnivorous fish have shorter tracts for digesting animal prey.\n\n10. Reproduction: Fish exhibit a wide range of reproductive strategies, including laying eggs, giving birth to live young (viviparity), and providing parental care.\n\n11. Diversity: Fish are an incredibly diverse group of animals, with over 30,000 known species. They vary in size, shape, color, behavior, and habitat, occupying a wide range of aquatic environments, from freshwater rivers and lakes to saltwater oceans and coral reefs.\n\nEcological Importance of Fish:\n\n1. Food Source: Fish are a vital food source for humans and other animals, providing protein, essential nutrients, and omega-3 fatty acids.\n\n2. Ecosystem Function: Fish play a crucial role in aquatic ecosystems by maintaining food webs, controlling populations of other aquatic organisms, and cycling nutrients.\n\n3. Nutrient Transfer: Fish transport nutrients between different parts of aquatic ecosystems, including from deep water to shallow water and from aquatic environments to terrestrial environments.\n\n4. Biodiversity: Fish contribute to the biodiversity of aquatic ecosystems, providing habitat and food sources for other organisms.\n\n5. Cultural Significance: Fish have cultural and economic significance for many human societies, featuring in art, literature, cuisine, and religious practices.\n\nFish are a diverse and ecologically important group of animals that play a vital role in maintaining the health and balance of aquatic ecosystems and providing sustenance for humans and other organisms. Their conservation and management are essential for ensuring the long-term sustainability of both natural ecosystems and the food security of human populations."
  },
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)