import { useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const ClassificationPage = () => {
    const [inputText, setInputText] = useState('');
    const [prediction, setPrediction] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const API_BASE_URL = 'http://localhost:8000/api/classification';

    const handlePredict = async () => {
        if (!inputText.trim()) {
            setError('Please enter some text');
            return;
        }

        setLoading(true);
        setError(null);
        setPrediction(null);

        try {
            const response = await axios.post(`${API_BASE_URL}/predict/`, {
                text: inputText,
            });
            setPrediction(response.data);
        } catch (err) {
            setError(err.response?.data?.error || 'Failed to classify document');
            console.error('Prediction error:', err);
        } finally {
            setLoading(false);
        }
    };

    const categories = ['Business', 'Entertainment', 'Health'];

    const testExamples = [
        // Clear category examples
        'The central bank increased interest rates to control inflation',
        'The actor won an award for his latest movie',
        'Doctors warn about rising cases of flu this winter',
        // Short examples
        'movie music actor',
        'stocks market economy',
        'doctor hospital patient',
        // All caps (robustness test)
        'THE ECONOMY AND THE MARKET',
        // Long example
        'Doctors and medical professionals across the country are warning patients about a new strain of influenza that is spreading rapidly during the winter season. Health officials recommend getting vaccinated and maintaining proper hygiene.',
        // Mixed topics
        'stocks vaccine film economy',
    ];

    return (
        <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100">
            <nav className="bg-white shadow-md border-b border-slate-200">
                <div className="max-w-7xl mx-auto px-6 py-4">
                    <div className="flex items-center justify-between">
                        <div className="flex items-center space-x-8">
                            <h1 className="text-2xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
                                Research Publication
                            </h1>
                            <div className="flex space-x-4">
                                <Link
                                    to="/"
                                    className="px-4 py-2 text-slate-600 hover:text-slate-900 hover:bg-slate-100 rounded-lg transition-all"
                                >
                                    🔍 Search Engine
                                </Link>
                                <Link
                                    to="/classification"
                                    className="px-4 py-2 bg-gradient-to-r from-blue-500 to-purple-500 text-white rounded-lg font-medium shadow-md"
                                >
                                    🧠 Document Classification
                                </Link>
                                <Link
                                    to="/stats"
                                    className="px-4 py-2 text-slate-600 hover:text-slate-900 hover:bg-slate-100 rounded-lg transition-all"
                                >
                                    📊 Statistics
                                </Link>
                            </div>
                        </div>
                    </div>
                </div>
            </nav>

            <div className="max-w-5xl mx-auto px-6 py-6">
                <div className="text-center mb-6">
                    <h2 className="text-3xl font-bold text-slate-900 mb-2">
                        Document Classification
                    </h2>
                    <p className="text-base text-slate-600 max-w-2xl mx-auto">
                        Enter a document and the Naïve Bayes classifier will predict its category.
                    </p>
                </div>

                <div className="bg-white rounded-2xl shadow-xl p-6 mb-6 border border-slate-200">
                    <label className="block text-sm font-semibold text-slate-700 mb-2">Enter Document Text</label>
                    <textarea
                        value={inputText}
                        onChange={(e) => setInputText(e.target.value)}
                        placeholder="Type or paste your text here..."
                        className="w-full h-24 px-4 py-3 border-2 border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none text-sm"
                    />

                    <div className="flex items-center justify-between mt-4">
                        <div className="text-xs text-slate-500">{inputText.length} characters</div>
                        <div className="flex space-x-3">
                            <button
                                onClick={() => { setInputText(''); setPrediction(null); setError(null); }}
                                className="px-5 py-2 bg-slate-100 text-slate-700 rounded-lg text-sm font-medium hover:bg-slate-200 transition-colors"
                            >
                                Clear
                            </button>
                            <button
                                onClick={handlePredict}
                                disabled={loading || !inputText.trim()}
                                className="px-6 py-2 bg-gradient-to-r from-blue-500 to-purple-500 text-white rounded-lg font-medium text-sm shadow-md hover:shadow-lg transition-all disabled:opacity-50"
                            >
                                {loading ? 'Classifying...' : 'Classify Document'}
                            </button>
                        </div>
                    </div>
                </div>

                {error && (
                    <div className="bg-red-50 border-l-4 border-red-500 p-4 mb-6 rounded-lg">
                        <div className="flex items-center"><span className="text-red-600 font-medium text-sm">❌ {error}</span></div>
                    </div>
                )}

                {prediction && !prediction.error && (
                    <div className="bg-white rounded-2xl shadow-xl p-6 mb-6 border border-slate-200">
                        <h3 className="text-lg font-bold text-slate-900 mb-4">Classification Result</h3>
                        <div className="flex items-center gap-6">
                            <div className="flex-1 p-4 rounded-xl border-2 bg-slate-50 border-slate-200">
                                <div className="text-xs font-medium uppercase tracking-wide text-slate-500">Predicted Category</div>
                                <div className="text-3xl font-bold mt-1 text-blue-700">{prediction.category}</div>
                                <div className="text-xs text-slate-500 mt-1">Confidence: {(prediction.confidence || 0).toFixed(4)}</div>
                            </div>

                            {prediction.probabilities && (
                                <div className="flex-1">
                                    <h4 className="text-sm font-semibold text-slate-700 mb-2">Class Probabilities</h4>
                                    <div className="space-y-2">
                                        {Object.entries(prediction.probabilities).map(([cat, p]) => (
                                            <div key={cat} className="flex items-center justify-between text-sm">
                                                <span className="text-slate-600">{cat}</span>
                                                <div className="flex items-center gap-2 flex-1 mx-3">
                                                    <div className="h-2 w-full bg-slate-100 rounded-full overflow-hidden">
                                                        <div
                                                            className="h-full bg-blue-500 rounded-full"
                                                            style={{ width: `${p * 100}%` }}
                                                        />
                                                    </div>
                                                </div>
                                                <span className="font-mono text-slate-700">{p.toFixed(4)}</span>
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            )}
                        </div>
                    </div>
                )}

                <div className="bg-white rounded-2xl shadow-xl p-6 border border-slate-200">
                    <h3 className="text-lg font-bold text-slate-900 mb-3">Try These Examples</h3>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                        {testExamples.map((t, i) => (
                            <button
                                key={i}
                                onClick={() => setInputText(t)}
                                className="p-3 rounded-xl border border-slate-200 bg-slate-50 text-left hover:border-blue-300 hover:bg-blue-50 transition-all group"
                            >
                                <div className="font-semibold text-xs text-slate-500 mb-1 group-hover:text-blue-600 transition-colors">Example {i + 1}</div>
                                <p className="text-xs text-slate-700 line-clamp-2">{t}</p>
                            </button>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ClassificationPage;
