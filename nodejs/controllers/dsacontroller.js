const { QuestionRequest } = require('../models/dsaRequest');
const DsaService = require('../services/dsaService');
const OpenAIService = require('../services/openaiService');

class DsaController {
    constructor() {
        const openaiService = new OpenAIService('your_openai_api_key_here', 'gpt-3.5-turbo');
        this.dsaService = new DsaService(openaiService);
    }

    registerRoutes(app) {
        app.post('/analyze_dsa', this.analyzeDsa.bind(this));
    }

    async analyzeDsa(req, res) {
        try {
            const questionRequest = new QuestionRequest(req.body);
            const analysis = await this.dsaService.analyzeQuestion(questionRequest);
            res.json({ question: questionRequest.question, analysis });
        } catch (error) {
            res.status(500).json({ error: error.message });
        }
    }
}

module.exports = DsaController;
