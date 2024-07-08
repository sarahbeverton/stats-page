<template>
    <div class="rvt-layout__wrapper [ rvt-p-tb-xl ]">
        <div class="rvt-container-lg">
            <div class="rvt-row">
                <div class="rvt-cols-12-md rvt-flow rvt-prose">
                    <div v-if="user.isLoggedIn.value">
                        <div class="rvt-row">
                            <div class="rvt-cols-4-md">
                                <div class="rvt-card">
                                    <div class="rvt-card__image hide-on-mobile">
                                        <img src="../assets/img/twitter_logo.png" style="background-color: white" alt="Twitter logo">
                                    </div>
                                    <div class="rvt-card__body">
                                        <h2 class="rvt-card__title">
                                            <a href="#tweets">OSoMe Tweets</a>
                                        </h2>
                                        <div class="rvt-card__content [ rvt-flow ]">
                                        <p>Tweets processed by OSoMe since May 2010</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="rvt-cols-4-md">
                                <div class="rvt-card">
                                    <div class="rvt-card__image hide-on-mobile tools">
                                        <img src="../assets/img/line-chart.png" alt="OSoMe tools logo">
                                    </div>
                                    <div class="rvt-card__body">
                                        <h2 class="rvt-card__title">
                                        <a href="#usage">OSoMe Usage</a>
                                        </h2>
                                        <div class="rvt-card__content [ rvt-flow ]">
                                        <p>Requests made to OSoMe tools, Moe's Tavern and Rapid API</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="rvt-cols-4-md">
                                <div class="rvt-card">
                                    <div class="rvt-card__image hide-on-mobile">
                                        <img src="../assets/img/twitter-robot-bird.png" alt="Botometer logo">
                                    </div>
                                    <div class="rvt-card__body">
                                        <h2 class="rvt-card__title">
                                            <a href="#botometer">Botometer</a>
                                        </h2>
                                        <div class="rvt-card__content [ rvt-flow ]">
                                            <p>Requests to the Botometer API through the Botometer website, the Rapid API, Hoaxy, etc.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <section id="tweets">
                            <legend class="rvt-legend [ rvt-ts-18 rvt-border-bottom rvt-p-bottom-xs ]">Tweet counts &nbsp;(Total processed: {{ totalTweetsProcessed.toLocaleString() }})</legend>
                            <!-- Accordion for pre_2016_counts -->
                            <div class="rvt-accordion" data-rvt-accordion="pre-2016-tweet-counts">
                                <h3 class="rvt-accordion__summary">
                                    <button class="rvt-accordion__toggle" data-rvt-accordion-trigger>
                                        <span class="rvt-accordion__toggle-text">Pre-2016 Tweet Counts &nbsp;(Tweets processed: {{ pre2016Total.toLocaleString() }})</span>
                                        <div class="rvt-accordion__toggle-icon">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                                                <g fill="currentColor">
                                                    <path class="rvt-accordion__icon-bar" d="M8,15a1,1,0,0,1-1-1V2A1,1,0,0,1,9,2V14A1,1,0,0,1,8,15Z" />
                                                    <path d="M14,9H2A1,1,0,0,1,2,7H14a1,1,0,0,1,0,2Z" />
                                                </g>
                                            </svg>
                                        </div>
                                    </button>
                                </h3>
                                <div class="rvt-accordion__panel" data-rvt-accordion-panel>
                                    <table>
                                        <thead>
                                        <tr>
                                            <th>Date</th>
                                            <th>Counts</th>
                                        </tr>
                                        </thead>
                                        <tbody>
                                        <tr v-for="(counts, date) in pre2016Counts" :key="date">
                                            <td>{{ date }}</td>
                                            <td>{{ counts }}</td>
                                        </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                            <div v-for="file in tweetCounts" :key="file.filename">
                                <div class="rvt-accordion" data-rvt-accordion="example-accordion">
                                    <h3 class="rvt-accordion__summary">
                                        <button class="rvt-accordion__toggle" data-rvt-accordion-trigger>
                                        <span class="rvt-accordion__toggle-text">{{ file.filename }} &nbsp;(Tweets processed: {{ calculateTotal(file.data).toLocaleString() }})</span>
                                        <div class="rvt-accordion__toggle-icon">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                                            <g fill="currentColor">
                                                <path class="rvt-accordion__icon-bar" d="M8,15a1,1,0,0,1-1-1V2A1,1,0,0,1,9,2V14A1,1,0,0,1,8,15Z" />
                                                <path d="M14,9H2A1,1,0,0,1,2,7H14a1,1,0,0,1,0,2Z" />
                                            </g>
                                            </svg>
                                        </div>
                                        </button>
                                    </h3>
                                    <div class="rvt-accordion__panel" data-rvt-accordion-panel>
                                        <table>
                                            <thead>
                                            <tr>
                                                <th>Date</th>
                                                <th>Counts</th>
                                            </tr>
                                            </thead>
                                            <tbody>
                                            <tr v-for="item in file.data" :key="item.date">
                                                <td>{{ item.date }}</td>
                                                <td>{{ item.value }}</td>
                                            </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                            
                        </section>
                        <section id="usage">
                            <legend class="rvt-legend [ rvt-ts-18 rvt-border-bottom rvt-p-bottom-xs ]">OSoMe Tools Request Counts</legend>
                            <div v-for="file in sortedRequestCounts" :key="file.filename">
                                <div class="rvt-accordion" data-rvt-accordion="example-accordion">
                                    <h3 class="rvt-accordion__summary">
                                        <button class="rvt-accordion__toggle" data-rvt-accordion-trigger>
                                        <span class="rvt-accordion__toggle-text">{{ file.displayName }}</span>
                                        <div class="rvt-accordion__toggle-icon">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                                            <g fill="currentColor">
                                                <path class="rvt-accordion__icon-bar" d="M8,15a1,1,0,0,1-1-1V2A1,1,0,0,1,9,2V14A1,1,0,0,1,8,15Z" />
                                                <path d="M14,9H2A1,1,0,0,1,2,7H14a1,1,0,0,1,0,2Z" />
                                            </g>
                                            </svg>
                                        </div>
                                        </button>
                                    </h3>
                                    <div class="rvt-accordion__panel" data-rvt-accordion-panel>
                                        <table>
                                            <thead>
                                            <tr>
                                                <th>Date</th>
                                                <th>Requests</th>
                                            </tr>
                                            </thead>
                                            <tbody>
                                            <tr v-for="item in file.data" :key="item.date">
                                                <td>{{ item.date }}</td>
                                                <td>{{ item.value }}</td>
                                            </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </section>
                        <section id="botometer">
                            <div>
                                <legend class="rvt-legend [ rvt-ts-18 rvt-border-bottom rvt-p-bottom-xs ]">Botometer</legend>
                                <div class="rvt-accordion" data-rvt-accordion="example-accordion">
                                    <h3 class="rvt-accordion__summary">
                                        <button class="rvt-accordion__toggle" data-rvt-accordion-trigger>
                                        <span class="rvt-accordion__toggle-text">Botometer Requests</span>
                                        <div class="rvt-accordion__toggle-icon">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                                            <g fill="currentColor">
                                                <path class="rvt-accordion__icon-bar" d="M8,15a1,1,0,0,1-1-1V2A1,1,0,0,1,9,2V14A1,1,0,0,1,8,15Z" />
                                                <path d="M14,9H2A1,1,0,0,1,2,7H14a1,1,0,0,1,0,2Z" />
                                            </g>
                                            </svg>
                                        </div>
                                        </button>
                                    </h3>
                                    <div class="rvt-accordion__panel" data-rvt-accordion-panel>
                                        <table>
                                            <thead>
                                            <tr>
                                                <th>Date</th>
                                                <th>Value</th>
                                            </tr>
                                            </thead>
                                            <tbody>
                                            <tr v-for="(stat, index) in botometerStats" :key="index">
                                                <td>{{ stat.date }}</td>
                                                <td>{{ stat.value }}</td>
                                            </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </section>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script lang="ts">
import axios from 'axios';
import { ref, onMounted, computed } from 'vue';
import { useUser } from '../composables/useUser'
import { useRouter, useRoute } from 'vue-router';

function parseBotometerStats(data: string) {
    return data.split('\n').map(line => {
        const [date, value] = line.split(',');
        if (!date || isNaN(Number(value))) {
            return null; // Skip invalid or empty lines
        }
        return { date, value: Number(value) };
    }).filter((entry): entry is { date: string, value: number } => entry !== null); // Remove null entries
}

function parseRequestCountStats(data: string) {
    return data.split('\n').map(line => {
        const [date, value] = line.split(':');
        if (!date || isNaN(Number(value))) {
            return null;
        }
        return { date, value: Number(value) };
    }).filter((entry): entry is { date: string, value: number } => entry !== null);
}

function parseTweetCountStats(data: string) {
    return data.split('\n').map(line => {
        const [date, value] = line.split(':');
        const parsedValue = Number(value);
        if (!date || isNaN(parsedValue)) {
            return null;
        }
        return { date, value: parsedValue };
    }).filter((entry): entry is { date: string, value: number } => entry !== null)
    .sort((a, b) => new Date(a.date).getTime() - new Date(b.date).getTime());
}


export default {
    setup() {
        const apiBaseUrl = import.meta.env.VITE_APP_API_BASE_URL;
        const user = useUser();
        const data = ref(null);
        const router = useRouter();
        const route = useRoute();
        const botometerStats = ref<{ date: string; value: number }[]>([]);
        const requestCounts = ref<{ filename: string, data: { date: string; value: number }[] }[]>([]);
        const tweetCounts = ref<{ filename: string, data: { date: string; value: number }[] }[]>([]);
        const searchQuery = ref(route.query.q || '');

        const getAllData = async () => {
            try {
                const response = await axios.get(`${apiBaseUrl}/api/stats/`);
                console.log("response", response)
                data.value = response.data
                if (response.data.botometer_stats) {
                    botometerStats.value = parseBotometerStats(response.data.botometer_stats);
                }
                if (response.data.request_counts) {
                    for (const [filename, fileData] of Object.entries(response.data.request_counts)) {
                        const parsedData = parseRequestCountStats(fileData as string);
                        requestCounts.value.push({ filename, data: parsedData });
                    }
                }
                if (response.data.tweetcounts) {
                    for (const [filename, fileData] of Object.entries(response.data.tweetcounts)) {
                        const parsedData = parseTweetCountStats(fileData as string);
                        tweetCounts.value.push({ filename, data: parsedData });
                    }
                }
            } catch (error) {
                console.error(`Error: ${error}`);
            }
        };

        const calculateTotal = (data: { date: string; value: number }[]) => {
            return data.reduce((total, item) => total + item.value, 0);
        }

        const pre2016Total = computed(() => {
            return calculateTotal(Object.values(pre2016Counts).map(value => ({ date: '', value })));
        });

        const totalTweetsProcessed = computed(() => {
            const tweetCountsTotal = tweetCounts.value.reduce((total, file) => {
                return total + calculateTotal(file.data);
            }, 0);

            return tweetCountsTotal + pre2016Total.value;
        });

        const sortedRequestCounts = computed(() => {
            return requestCounts.value.slice().sort((a, b) => {
                const yearA = a.filename.match(/\d{4}$/);
                const yearB = b.filename.match(/\d{4}$/);

                if (yearA && yearB) {
                    return parseInt(yearA[0], 10) - parseInt(yearB[0], 10);
                } else if (yearA) {
                    return -1;
                } else if (yearB) {
                    return 1;
                } else {
                    return a.filename.localeCompare(b.filename);
                }
            }).map(item => {
                const yearMatch = item.filename.match(/\d{4}$/);
                if (yearMatch) {
                    return { ...item, displayName: yearMatch[0] };
                } else {
                    return { ...item, displayName: "Moe's Tavern" };
                }
            });
        });

        const pre2016Counts = {
            "2010-05": 38873143,
            "2010-06": 76865997,
            "2010-07": 62258497,
            "2010-08": 103045756,
            "2010-09": 211834712,
            "2010-10": 234171013,
            "2010-11": 229205281,
            "2010-12": 259644433,
            "2011-01": 291569068,
            "2011-02": 293416918,
            "2011-03": 376197856,
            "2011-04": 346974159,
            "2011-05": 445130767,
            "2011-06": 383655582,
            "2011-07": 540524599,
            "2011-08": 575558981,
            "2011-09": 559155670,
            "2011-10": 521485083,
            "2011-11": 674989818,
            "2011-12": 708145559,
            "2012-01": 742942706,
            "2012-02": 738505770,
            "2012-03": 909012147,
            "2012-04": 1002828827,
            "2012-05": 1068704214,
            "2012-06": 1004501053,
            "2012-07": 1123056658,
            "2012-08": 953711214,
            "2012-09": 1108744517,
            "2012-10": 1048528657,
            "2012-11": 1126020063,
            "2012-12": 708145559,
            "2013-01": 1425863771,
            "2013-02": 1297390880,
            "2013-03": 1441824688,
            "2013-04": 1442315017,
            "2013-05": 1203691558,
            "2013-06": 1483879315,
            "2013-07": 1602553145,
            "2013-08": 1617812154,
            "2013-09": 1427186850,
            "2013-10": 1465718947,
            "2013-11": 1169491740,
            "2013-12": 1054831380,
            "2014-01": 1136645429,
            "2014-02": 895839235,
            "2014-03": 1228535923,
            "2014-04": 1365018707,
            "2014-05": 1245085753,
            "2014-06": 1445894448,
            "2014-07": 1341874907,
            "2014-08": 1419527375,
            "2014-09": 1353898826,
            "2014-10": 1416182347,
            "2014-11": 1217756473,
            "2014-12": 1394874464,
            "2015-01": 1340196516,
            "2015-02": 1280701157,
            "2015-03": 1404883671,
            "2015-04": 1117120660,
            "2015-05": 865560193,
            "2015-06": 1295125546,
            "2015-07": 1319360163,
            "2015-08": 1377316413,
            "2015-09": 1235483854,
            "2015-10": 1250984863,
            "2015-11": 1225476380,
            "2015-12": 1307455927,
            "2016-01": 1242469695,
            "2016-02": 1205656440,
            "2016-03": 1203449614,
            "2016-04": 1188976365,
            "2016-05": 1140169564,
            "2016-06": 1176632841,
            "2016-07": 1217591905
        };

        onMounted(() => {
            if (user.isLoggedIn.value) {
                getAllData();
            } else {
                router.push('/');
            }
        });

        return {
            apiBaseUrl,
            user,
            data,
            botometerStats,
            requestCounts,
            sortedRequestCounts,
            tweetCounts,
            pre2016Counts,
            pre2016Total,
            totalTweetsProcessed,
            getAllData,
            calculateTotal
        };
    }
};
</script>

<style scoped>
.rvt-card__image.tools {
    position: relative;
    width: 100%;
    max-width: 300px;
    height: 0;
    padding-top: 100%;
    overflow: hidden;
    background-color: #ffffff;
}

.rvt-card__image.tools img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: contain;
}

.rvt-accordion__summary {
    padding: 0.5rem 1rem;
}

.rvt-accordion__toggle {
    padding: 0.5rem;
    margin: 0;
}

.rvt-accordion__toggle-text {
    font-size: 14px;
}

.rvt-accordion__toggle-icon {
    padding: 0.2rem;
}

.rvt-accordion__panel {
    padding: 0.2rem 0rem;
}

td {
    padding: 1em 1em;
    font-size: 14px;
}

#botometer {
    margin-top: 4em;
    margin-bottom: 2em;
}

#usage {
    margin-top: 4em;
}

#tweets {
    margin-top: 5em;
}

@media (max-width: 767px) {
    .hide-on-mobile {
        display: none;
    }
}

</style>
  