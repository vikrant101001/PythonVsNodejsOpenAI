const OpenAIService = require('./openaiService');
const { QuestionRequest } = require('../models/dsaRequest');

class DsaService {
    constructor(openaiService) {
        this.openaiService = openaiService;
    }

    async analyzeQuestion(questionRequest) {
        const basePrompt = `
        You are a DSA expert. Given a question related to Data Structures and Algorithms (DSA),
        identify the topics being asked and provide an explanation for it. Respond in a structured
        format with a list of topics and an explanation.
        `;
        const fullPrompt = `${basePrompt}\n\nQuestion: ${questionRequest.question}`;
        return await this.openaiService.analyzeDsa(fullPrompt);
    }
}

module.exports = DsaService;
