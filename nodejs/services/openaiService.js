const openai = require('openai');

class OpenAIService {
    constructor(apiKey, model) {
        this.apiKey = apiKey;
        this.model = model;
        this.client = new openai.OpenAI(apiKey);
    }

    async analyzeDsa(prompt) {
        try {
            const response = await this.client.chatCompletions.create({
                model: this.model,
                messages: [{ role: 'user', content: prompt }]
            });
            return response.choices[0].message.content;
        } catch (error) {
            throw new Error('Failed to analyze DSA question: ' + error.message);
        }
    }
}

module.exports = OpenAIService;
